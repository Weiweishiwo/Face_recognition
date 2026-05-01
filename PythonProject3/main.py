import database_connect
import records

# code = input("选择：")
#
# match code:
#     case '1':# 增加
#         # name = input("请输入姓名：")
#         # id = input("请输入学号：")
#         print(database_connect.insert_student(6024203466,"刘飞"))
#     case '2':# 删除
#         id = input("请输入学号：")
#         name = input("请输入姓名：")
#         print(database_connect.delete_student(id, name))
#     case '3':# 更新
#         id = input("请输入学号：")
#         name = input("请输入姓名：")
#         print(database_connect.update_student(id, name))
#     case '4':# 查找
#         id = input("请输入学号：")
#         print(database_connect.select_student(id))


























student_id = "6024203466"
student_name = "刘飞"

rec = records.AttendanceRecord(student_id, student_name)
# rec.sign_in()   # 签到
rec.sign_out()  # 用同一个 rec 签退



# print(http_status_text(404))        # Not Found
#
# # 查找
# id = input("请输入学号：")
# print(database_connect.select_student(id))
#
# # 增加
# name = input("请输入姓名：")
# print(database_connect.insert_student(id, name))
#
# # 删除
# print(database_connect.delete_student(id, name))
#
# # 更新
# print(database_connect.update_student(id, name))














