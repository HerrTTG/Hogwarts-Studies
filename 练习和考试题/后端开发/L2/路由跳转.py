"""
使用 url_for() 生成 url ，再使用 redirect() 方法完成路径的重定向。实现当完成添加的逻辑后，跳转展示的逻辑。
"""

from flask import Flask, url_for, Blueprint, redirect

app = Flask(__name__)

home_index = Blueprint(name='index', import_name=__name__, url_prefix="/index")


# 直接生成

@app.route("/login")
def login():
    return redirect(url_for("login2"))


@app.route("/login2")
def login2():
    return redirect(url_for("index.index"))


@home_index.route("")
def index():
    print("首页")
    return {"code": 0, "msg": "success"}


if __name__ == '__main__':
    app.register_blueprint(home_index)
    app.run("0.0.0.0", port=5050)
