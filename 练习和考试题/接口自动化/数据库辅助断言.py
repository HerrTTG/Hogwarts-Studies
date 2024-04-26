import pymysql


# 二次封装数据库相关的操作

class Dblink():

    # 封装建立连接的对象
    @classmethod
    def get_conn(cls):
        # conn = pymysql.connect(
        # host="litemall.hogwarts.ceshiren.com",
        # port=13306,
        # user="test",
        # password="test123456",
        # database="litemall",
        # charset="utf8mb4"
        # )
        conn = pymysql.Connect(host='localhost', port=3306,
                               user='root', password='Kuoka314+', database='hogwarts', charset='utf8')
        return conn

    # 执行sql语句
    @classmethod
    def execute_sql(cls, sql):
        connect = Dblink.get_conn()
        cursor = connect.cursor()
        cursor.execute(sql)  # 执行SQL
        record = cursor.fetchall()  # 查询记录
        return record


if __name__ == '__main__':
    # 执行sql语句查询user123这个用户的购物车有一个名称为 hogwarts1 的商品
    # print(Dblink.execute_sql("select * from litemall_cart where "
    #             "user_id=1 and deleted=0 and "
    #             "goods_name='hogwarts1'"))

    res = Dblink.execute_sql("select * from students;")

    # 多结果断言
    for i in res:
        try:
            assert 'xueqing' in i
        except:
            continue
        else:
            print(i)
            break
    else:
        raise AssertionError
