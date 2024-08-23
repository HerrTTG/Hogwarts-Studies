from flask import Flask

# 创建 Flask 应用程序实例
api = Flask(__name__)


# 定义路由和视图函数
@api.route("/")
def hello():
    return "Hello Flask!"


if __name__ == '__main__':
    api.run()
