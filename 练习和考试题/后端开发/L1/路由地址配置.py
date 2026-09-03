from flask import Flask, escape

# 创建 Flask 应用程序实例
API = Flask(__name__)


# 定义基本路由
@API.route("/")
def index():
    """根目录"""
    return "Home Page"


@API.route("/about")
def about():
    """某path"""
    return "About Page"


@API.route("/user/<username>")
def user_info(username):
    """
    动态路由
    比如路由 /user后面想要根据不同的用户名，返回不同的数据
    """
    return f"User {username} is select info."


# 限定类型的动态路由
# 类型限定为整型
@API.route("/user/<int:user_id>")
def user_id(user_id):
    # 展示给定的用户 ID，ID 为整型（输出前做 HTML 转义，避免反射型 XSS）
    safe_user_id = escape(str(user_id))
    return f"User ID is {safe_user_id}"


# 类型限定为 path（可以包含 /）
@API.route('/path/<path:sub_path>')
def show_subpath(sub_path):
    # 展示 path 后的子路由（对用户输入做 HTML 转义，避免反射型 XSS）
    return f'Subpath is {escape(sub_path)}'


# 运行应用程序
if __name__ == '__main__':
    API.run()
