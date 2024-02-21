import pymysql

db_connect = pymysql.Connect(host='localhost', port=3306,
                             user='root', password='Kuoka314+', database='hogwarts', charset='utf8')
# 游标对象
# 通过游标来进行数据库操作
cursor = db_connect.cursor()

cursor.execute('''select * from students where sid=1;''')

# 单条查询 每次查询游标会自动游标下移
# result=cursor.fetchone()
# print(result)
# result=cursor.fetchone()
# print(result)
# result=cursor.fetchone()
# print(result)

# 全部查询
result = cursor.fetchall()
print(result)

# 多个数据查询 和单次查询一样，游标会自动下移
# result = cursor.fetchmany(1)
# print(result)
# result = cursor.fetchmany(1)
# print(result)
# result = cursor.fetchmany(1)
# print(result)

db_connect.close()
