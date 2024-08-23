from flask import Flask, request

# 创建 Flask 应用程序实例
API = Flask(__name__)


# get 请求
@API.route("/get")
def get():
    """路由装饰器后不限定method默认为get"""
    return f"Method is GET."


@API.route("/get_method", methods=["GET"])
def get_method():
    return f"GET method success."


@API.route("/info", methods=["POST", "PUT"])
def update():
    return f"Method is {request.method}."


if __name__ == '__main__':
    API.run()
