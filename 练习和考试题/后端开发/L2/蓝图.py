from flask import Blueprint, Flask

app = Flask(__name__)
user_router = Blueprint("user", __name__, url_prefix="/user")
"""
Flask 中的蓝图（Blueprint）是一种组织和管理应用程序路由和视图的机制。
它允许开发者将相关功能的路由和视图进行分组，从而更好地组织项目结构和实现模块化开发。
蓝图可以极大地简化大型应用并为扩展提供集中的注册入口。

Flask 可以通过蓝图来组织 URL 以及处理请求。如果使用蓝图，应用会在 Flask 层中进行管理，共享配置，通过注册按需改变应用对象。
蓝图的缺点是一旦应用被创建后，只有销毁整个应用对象才能注销蓝图。

一个项目可以具有多个蓝图。但是一个蓝图并不是一个完整的应用，它不能独立于应用运行，而必须要注册到某一个应用中。
"""


@user_router.route("")
def user_list():
    """因为在蓝图已经定义了url的前缀为/user,所以这里的路由设置路径为空，就是相当于直接访问/user"""
    return {"code": 0, "msg": "get success", "data": []}


@user_router.route("/login", methods=["POST"])
def login():
    """/user/login"""
    return {"code": 0, "msg": "login success"}


if __name__ == '__main__':
    # 注册蓝图
    app.register_blueprint(user_router)
    app.run(port=5055, debug=True)
