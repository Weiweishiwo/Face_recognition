import pymysql
from pymysql.cursors import DictCursor

DB_CONFIG = {
    'host':'localhost',
    'user':'root',
    'password':'Pan1261949598.',
    'database':'face_attendance',
    'charset':'utf8',
    'cursorclass':DictCursor
}

def get_conn():
    return pymysql.connect(**DB_CONFIG)

# id是存储变量
# id = '0000000001'

# name也是存储变量
# name = '潘世玮'

def select_student(student_id):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from student where student_id=%s', (student_id,))
            return cursor.fetchone()
    finally:
        conn.close()

def insert_student(student_id, name):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute('insert into student (student_id, name) values (%s, %s)', (student_id, name))
            conn.commit()
            return "插入成功"
    except Exception as e:
        conn.rollback()
        return f"插入失败：{e}"
    finally:
        conn.close()

def delete_student(student_id, name=None):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            if name:
                sql = "DELETE FROM student WHERE student_id = %s AND name = %s"
                affected = cursor.execute(sql, (student_id, name))
            else:
                sql = "DELETE FROM student WHERE student_id = %s"
                affected = cursor.execute(sql, (student_id,))
            conn.commit()
            return affected
    except Exception as e:
        conn.rollback()
        raise e          # 可以选择重新抛出异常让上层处理
    finally:
        conn.close()


def update_student(student_id, name):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE student SET name = %s WHERE student_id = %s"
            affected = cursor.execute(sql, (name, student_id))
            conn.commit()
            return affected   # 返回受影响行数
    except Exception as e:
        conn.rollback()
        print(f"更新失败: {e}")
        return 0
    finally:
        conn.close()


def insert_sign_record(student_id, student_name, sign_time, status=1):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO sign (student_id, student_name, sign_time, status)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (student_id, student_name, sign_time, status))
            conn.commit()
            return cursor.lastrowid
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def update_sign_out(record_id, sign_out_time):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            # 原来可能是 sign_out，改为 sign
            sql = """
                UPDATE sign
                SET sign_out_time = %s, status = 2
                WHERE sign_id = %s
            """
            cursor.execute(sql, (sign_out_time, record_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def get_today_record(student_id, today_str):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT * FROM sign
                WHERE student_id = %s AND DATE(sign_time) = %s
                ORDER BY sign_id DESC LIMIT 1
            """
            cursor.execute(sql, (student_id, today_str))
            return cursor.fetchone()
    finally:
        conn.close()
