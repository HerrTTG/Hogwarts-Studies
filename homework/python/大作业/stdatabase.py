import json
import pymysql
from pymysql import err


class ManagementDB:
    def __init__(self, user='root', pwd='123123', host='localhost', port=3306, database='hogwarts'):
        # 类被实例化时连接数据库
        self.db_connect = pymysql.Connect(host=host, port=port,
                                          user=user, password=pwd, database=database, charset='utf8')
        self.cursor = self.db_connect.cursor()

    def __del__(self):
        # 类的对象被删除时断开数据库
        self.db_connect.close()

    def st_add(self, values):
        # 学生数据新增
        # sid=01&name=lucy&age=23&gender=male
        sid = values.get('sid')
        name = values.get('name')
        age = values.get('age')
        gender = values.get('gender')
        try:
            # name age gender必须有一个数据不为空 才算合理的新增数据。否则只有sid。
            assert name or age or gender
            self.cursor.execute('''insert into students set sid=%s,name=%s,age=%s,gender=%s'''
                                , (sid, name, age, gender))
        except err.IntegrityError:
            return f'Data insert failed,Duplicate key sid {sid}.'.encode()

        except AssertionError:
            return 'Data insert failed,name age or gender not have any content.'.encode()
        else:
            self.cursor.execute('''select * from  students where sid=%s''', sid)
            if self.cursor.fetchall():
                self.db_connect.commit()
                return 'Data insert success'.encode()

    def st_change(self, values):
        # 学生数据修改
        # sid=01&name=kevin&age=23&gender=male
        sid = values.get('sid')
        name = values.get('name')
        age = values.get('age')
        gender = values.get('gender')
        try:
            self.cursor.execute('''select * from  students where sid=%s''', sid)
            assert self.cursor.fetchall()
        except AssertionError:
            return f'Data update failed,{sid} not exists in database'.encode()
        else:
            try:
                assert name or age or gender
            except AssertionError:
                return f'Data update failed,name、age、gender not have any content.'.encode()
            else:
                if name:
                    self.cursor.execute('''update students set name=%s where sid=%s''',
                                        (name, sid))
                if age:
                    self.cursor.execute('''update students set age=%s where sid=%s''',
                                        (age, sid))
                if gender:
                    self.cursor.execute('''update students set gender=%s where sid=%s''',
                                        (gender, sid))

            # 检查数据是否修改正确
            self.cursor.execute('''select * from  students where sid=%s''', sid)
            result = self.cursor.fetchall()

            # ((1, 'haizhenyu', '29', 'male'),)
            for i in result:
                if i:
                    try:
                        assert str(i[0]) == sid
                        if name:
                            assert i[1] == name
                        if age:
                            assert i[2] == age
                        if gender:
                            assert i[3] == gender
                    except AssertionError:
                        return f'Update failed,datas not changed correct.'.encode()
            else:
                self.db_connect.commit()
                return 'Data update success'.encode()

    def st_query(self, values):
        # 学生数据查询
        # sid=s09
        # {'sid':s09}
        sid = values.get('sid')
        try:
            if sid == 'all':
                self.cursor.execute('''select * from students;''')
            else:
                self.cursor.execute('''select * from students where sid=%s;''', sid)

            results = self.cursor.fetchall()
            assert results
        except AssertionError:
            return 'Data not found'.encode()
        else:
            # ((1, 'haizhenyu', '29', 'male'), (2, 'xueqing', '27', 'fmale'))
            response_list = list()
            for i in results:
                response = dict()
                response['sid'] = i[0]
                response['name'] = i[1]
                response['age'] = i[2]
                response['gender'] = i[3]
                response_list.append(response)
            return json.dumps(response_list).encode()

    def st_del(self, values):
        # 学生数据删除
        sid = values.get('sid')
        try:
            self.cursor.execute('''select * from students where sid=%s;''', sid)
            results = self.cursor.fetchall()
            assert results
        except AssertionError:
            return 'Delete datas failed,Data not found'.encode()
        else:
            try:
                self.cursor.execute('''delete from students where sid=%s''', sid)
                self.cursor.execute('''select * from students where sid=%s;''', sid)
                results = self.cursor.fetchall()
                assert results == ()
            except AssertionError:
                return 'Data delete failed,datas still exits in database.'.encode()
            else:
                self.db_connect.commit()
                return 'Data delete success'.encode()
