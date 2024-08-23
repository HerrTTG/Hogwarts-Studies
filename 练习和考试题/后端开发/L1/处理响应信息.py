from flask import Flask, jsonify, render_template, make_response

# 创建 Flask 应用程序实例
API = Flask(__name__)


# 定义路由和视图函数
@API.route('/text')
def text_res():
    return '返回文本'


@API.route('/tuple')
def tuple_res():
    """元组格式包含 3 个参数类型。第一个是 response 对象，第二个是响应状态码，第三个是响应头信息"""
    return "你好呀", 200, {"hogwarts": "Harry"}


@API.route('/dict')
def get_dict():
    "返回字典对象在 Flask 1.1 版本之后，Flask 会调用 jsonify() 方法转为json格式"
    return {'status': 0}


@API.route('/json')
def get_json():
    """或者用jsonify方法进行转换"""
    """支持传入字典转json，也支持key=value传入"""
    # jsonify({'status': 0})
    return jsonify(status=1, name="lily", age=20)


@API.route('/html')
def get_html():
    # 调用render_template方法，传入html 文件的名称。
    # 注意html文件必须在 templates 目录下
    return render_template('demo.html')


@API.route('/')
def index():
    resp = make_response(render_template('demo.html'))
    # 设置cookie
    resp.set_cookie('username', 'the username')
    # 设置响应头信息
    resp.headers["hogwarts"] = "HAI"
    return resp


# 运行应用程序
if __name__ == '__main__':
    API.run()
