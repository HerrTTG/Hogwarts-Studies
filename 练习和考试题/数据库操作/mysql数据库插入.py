import pymysql

db_connect = pymysql.Connect(host='localhost', port=3306,
                             user='root', password='Kuoka314+', database='hogwarts', charset='utf8')
# 游标对象
# 通过游标来进行数据库操作
cursor = db_connect.cursor()

# 添加进入数据库的变量
values = (4, "wangwang")

# 执行insert
result = cursor.execute('''insert into students(id,name) values(%s,%s)''', values)
print(result)

# 查询结果
cursor.execute('''select * from students;''')
print(cursor.fetchall())

# commit
db_connect.commit()

# 断开连接
db_connect.close()
