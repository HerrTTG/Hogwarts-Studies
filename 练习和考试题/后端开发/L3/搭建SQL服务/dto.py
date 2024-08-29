from pymysql import Connect

db_connect = Connect(host='localhost', port=3306,
                     user='root', password='Kuoka314+', database='hogwarts', charset='utf8mb4')


class Db_serve:
    def search_serve(self, sql_str, value_list):
        cursor = db_connect.cursor()
        cursor.execute(sql_str, value_list)
        result = cursor.fetchall()
        cursor.close()
        return [{"sid": item[0], "name": item[1], "age": item[2], "gender": item[3]} for item in result]

    def update_serve(self, sql_str, value_list):
        cursor = db_connect.cursor()
        num = cursor.execute(sql_str, value_list)
        db_connect.commit()
        cursor.close()
        return num

    def insert_serve(self, sql_str, value_list):
        cursor = db_connect.cursor()
        num = cursor.execute(sql_str, value_list)
        db_connect.commit()
        cursor.close()
        return num
