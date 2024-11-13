import pymysql

from Dbtools.tools import insert_data, tabale_infos


def expecterr(func):
    def inner(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
        except:
            pass
        else:
            if value:
                return value
            else:
                return True

    return inner


class Dbconnect():
    # 数据获取委托出去
    __table_info = tabale_infos
    __insert_data = insert_data
    db_connect = pymysql.Connect(host='localhost', port=3306,
                                 user='root', password='Kuoka314+', database='hogwarts', charset='utf8')

    def __init__(self, cursor=None):
        if cursor is not None:
            self.cursor = cursor
        else:
            self.cursor = self.db_connect.cursor()

    @expecterr
    def create_tables(self):
        for item, value in self.__table_info.items():
            self.cursor.execute(value)

    @expecterr
    def insert_data(self):
        for table in self.check_empty():
            insert_query = ""
            if table == "Student":
                insert_query = f"INSERT INTO {table}  (SId,Sname, Sage, Ssex) VALUES (%s, %s, %s, %s);"
            elif table == "Course":
                insert_query = f"INSERT INTO {table}  (CId,Cname, TId) VALUES (%s,%s,%s);"
            elif table == "Teacher":
                insert_query = f"INSERT INTO {table}  (TId,Tname) VALUES (%s,%s);"
            elif table == "SC":
                insert_query = f"INSERT INTO {table}  (SId,CId,score) VALUES (%s,%s,%s);"

            data = self.__insert_data[table]
            self.cursor.executemany(insert_query, data)
            self.commit()

    @expecterr
    def check_empty(self):
        for table in self.__table_info.keys():
            query = f"SELECT COUNT(*) AS count FROM {table};"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result[0] == 0:
                yield table

    def commit(self):
        self.db_connect.commit()

    #
    # def close(self):
    #     self.db_connect.close()

    @expecterr
    def query(self, commd, fetch_all=True):
        self.cursor.execute(commd)
        if fetch_all:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()
