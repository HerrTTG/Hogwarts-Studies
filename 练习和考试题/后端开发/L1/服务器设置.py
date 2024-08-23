from flask import Flask, render_template, make_response

# 创建 Flask 应用程序实例
API = Flask(__name__)


@API.route('/')
def index():
    resp = make_response(render_template('demo.html'))
    # 设置cookie
    resp.set_cookie('username', 'the username')
    # 设置响应头信息
    resp.headers["hogwarts"] = "HAI"
    return resp


"""
0.0.0.0 开启局域网访问模式，由本机IP地址进行访问。可设置端口，debug模式开启
"""
API.run(host="0.0.0.0", port=5050, debug=True)
