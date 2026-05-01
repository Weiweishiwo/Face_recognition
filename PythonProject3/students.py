class student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.name = student_name


    @classmethod
    def from_db_row(cls, row):
        """从数据库查询结果（元组或字典）创建对象"""
        return cls(row[0], row[1])