import json
from flask import Blueprint, render_template, request, url_for, redirect
from pymysql import *

# 1. 蓝图的声明
bookBP = Blueprint(name="book", import_name=__name__, url_prefix="/book")
# 连接数据库
db_connect = Connect(host='localhost', port=3306,
                     user='root', password='Kuoka314+', database='hogwarts', charset='utf8mb4')


# 通过蓝图来管理数据接口

# 首页接口
@bookBP.route("")
def index():
    return render_template("index.html")


# 首页数据接口
@bookBP.route("/list")
def data_list():
    # 查询数据库得到所有的数据展示
    # 获取游标对象
    cursor = db_connect.cursor()
    sql_str = ''' select * from book; '''
    cursor.execute(sql_str)
    datas = cursor.fetchall()
    cursor.close()
    result = [{"bid": item[0], "name": item[1], "price": item[2], "summary": item[3], "quantity": item[4]} for item in
              datas]
    return json.dumps(result, ensure_ascii=False)

# 添加页面接口，和添加数据接口
@bookBP.route("/add", methods=["GET", "POST"])
def add():
    # 根据请求方式区别不同的操作
    if request.method == "GET":
        return render_template("add.html")
    else:
        # 将添加提交过来的数据保存到数据库中
        bid = request.json.get("bid")
        name = request.json.get("name")
        price = request.json.get("price")
        summary = request.json.get("summary")
        quantity = request.json.get("quantity")

        sql_str = ''' insert into book(bid, name, price, summary, quantity) values(%s,%s,%s,%s,%s) ;'''
        cursor = db_connect.cursor()
        cursor.execute(sql_str, [bid, name, price, summary, quantity])
        # 提交更改操作，不提交不声效
        db_connect.commit()
        cursor.close()
        return redirect(url_for("book.index"))


# 修改数据接口
@bookBP.route("/change/<bid>", methods=["GET", "POST"])
def change(bid):
    # 根据请求方式区别不同的操作
    if request.method == "GET":
        return render_template("change.html")
    else:
        # 将数据库中的数据找出来修改后再保存到数据库中
        # 将添加提交过来的数据保存到数据库中
        name = request.json.get("name")
        price = request.json.get("price")
        summary = request.json.get("summary")
        quantity = request.json.get("quantity")
        sql_str = ''' update book set name=%s, price=%s, summary=%s, quantity=%s where bid = %s ;'''
        cursor = db_connect.cursor()
        cursor.execute(sql_str, [name, price, summary, quantity, bid])
        # 提交更改操作，不提交不声效
        db_connect.commit()
        cursor.close()
        return redirect(url_for("book.index"))


# 用来返回修改信息时的回显数据
@bookBP.route("/chageData/<bid>")
def changeData(bid):
    cursor = db_connect.cursor()
    sql = f'''select * from book where bid = {bid};'''
    cursor.execute(sql)
    item = cursor.fetchone()
    cursor.close()
    result = {"bid": item[0], "name": item[1], "price": item[2], "summary": item[3], "quantity": item[4]}
    return json.dump(result, ensure_ascii=False)


# 删除信息接口
@bookBP.route("/delete/<bid>")
def delete(bid):
    curosr = db_connect.cursor()
    sql = ''' delete from book where bid = %s ;'''
    curosr.execute(sql, [bid])
    db_connect.commit()
    curosr.close()
    return redirect(url_for("book.index"))


# 搜索接口
@bookBP.route("/search")
def search():
    wd = f'%{request.json.get("wd")}%'  # %python%  like 语法模糊搜索%内容%
    cursor = db_connect.cursor()
    sql = ''' select * from book where name like %s or summary like %s'''
    cursor.execute(sql, [wd, wd])
    datas = cursor.fetchall()
    cursor.close()
    result = [{"bid": item[0], "name": item[1], "price": item[2], "summary": item[3], "quantity": item[4]} for item in
              datas]
    return json.dumps(result, ensure_ascii=False)
