import pymysql

db_connect = pymysql.Connect(host='localhost', port=3306,
                             user='root', password='Kuoka314+', database='hogwarts', charset='utf8')
# 游标对象
# 通过游标来进行数据库操作
cursor = db_connect.cursor()

# 更新数据
values = [4]
cursor.execute('''delete from students where id=%s''', values)

# 查询结果
cursor.execute('''select * from students;''')
print(cursor.fetchall())

db_connect.commit()
