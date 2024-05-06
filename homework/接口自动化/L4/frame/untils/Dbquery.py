import pymysql


# 二次封装数据库相关的操作

class Dblink():

    def __init__(self, envinfo):
        """
        实例化环境信息，从环境信息中获取baseurl
        生成request方法的对象
        """
        self.envinfo = envinfo
        self.baseurl = self.envinfo['url']
        self.dbinfo = self.envinfo['dbinfo']

    # 封装建立连接的对象

    def get_conn(self):
        # conn = pymysql.connect(
        # host="litemall.hogwarts.ceshiren.com",
        # port=13306,
        # user="test",
        # password="test123456",
        # database="litemall",
        # charset="utf8mb4"
        # )
        conn = pymysql.Connect(**self.dbinfo)
        return conn

    # 执行sql语句
    def execute_sql(self, sql):
        connect = self.get_conn()
        cursor = connect.cursor()
        cursor.execute(sql)  # 执行SQL
        record = cursor.fetchall()  # 查询记录
        return record
