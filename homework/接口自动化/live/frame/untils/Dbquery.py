import pymysql


# 二次封装数据库相关的操作

class Dblink():

    def __init__(self, envinfo):
        """
        实例化环境信息，从环境信息中获取数据库连接需要的信息
        dbinfo: { 'host': 'localhost','port': 3306,'user': 'root',
        'password': 'Kuoka314+','database': 'hogwarts','charset': 'utf8' }
        解包传入，创建数据库链接对象
        """
        self.conn = pymysql.Connect(**envinfo['dbinfo'])

    # 执行sql语句
    def execute_sql(self, sql) -> object:
        """
        sql执行方法，先创建游标。在执行具体sql。
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)  # 执行SQL
        # record = cursor.fetchall()  # 查询记录
        return cursor
