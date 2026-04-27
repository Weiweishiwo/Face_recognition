import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Pan1261949598.',
    database='face_attendance',
    charset='utf8'
)

# id是存储变量
# id = '0000000001'

# name也是存储变量
name = '潘世玮'

def select_student(id):
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from student where student_id=%s', (id))
            result = cursor.fetchone()
            # print(result)
            return result
    finally:
        conn.close()

def insert_student(id, name):
    try:
        with conn.cursor() as cursor:
            cursor.execute('insert into student (student_id, name) values (%s, %s)', (id, name))
            conn.commit()
            return "插入成功"
    except Exception as e:
        conn.rollback()
        return f"插入失败：{e}"
    finally:
        cursor.close()
        conn.close()

def delete_student(student_id, name):
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM student WHERE student_id = %s AND name = %s"
            affected = cursor.execute(sql, (student_id, name))
            conn.commit()
            return affected
    except Exception as e:
        conn.rollback()
        raise e          # 可以选择重新抛出异常让上层处理
    finally:
        conn.close()


def update_student(student_id, name):
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
