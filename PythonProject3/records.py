from datetime import datetime, date
import database_connect


class AttendanceRecord:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.sign_time = None
        self.sign_out_time = None
        self.status = 0
        self.record_id = None
        self._load_today_record()

    def _load_today_record(self):
        today_str = date.today().isoformat()
        record = database_connect.get_today_record(self.student_id, today_str)
        if record:
            self.record_id = record['sign_id']
            self.sign_time = record['sign_time']
            self.sign_out_time = record.get('sign_out_time')
            self.status = record['status']


    def sign_in(self):
        self.sign_time = datetime.now()
        self.status = 1
        sign_time_str = self.sign_time.strftime('%Y-%m-%d %H:%M:%S')
        try:
            self.record_id = database_connect.insert_sign_record(
                self.student_id, self.student_name, sign_time_str, 1
            )
            print(f"签到成功，数据库记录ID：{self.record_id}")
        except Exception as e:
            # 回滚内存状态（可选）
            self.status = 0
            self.sign_time = None
            self.record_id = None
            print(f"签到数据库写入失败：{e}")
            return None
        return self.sign_time

    def sign_out(self):
        """签退操作"""
        if self.status == 0:
            print("尚未签到，无法签退")
            return None
        if self.status == 2:
            print("已经签退过了，无需重复签退")
            return self.sign_out_time

        # 必须有对应的签到记录ID才能更新
        if self.record_id is None:
            print("没有可签退的记录")
            return None
        if self.status == 2:
            print("该记录已经签退过")
            return self.sign_out_time
        self.sign_out_time = datetime.now()
        sign_out_time_str = self.sign_out_time.strftime('%Y-%m-%d %H:%M:%S')
        try:
            database_connect.update_sign_out(self.record_id, sign_out_time_str)
            self.status = 2
            print(f"签退成功，时间：{self.sign_out_time}")
        except Exception as e:
            print(f"签退失败：{e}")
            return None
        return self.sign_out_time

