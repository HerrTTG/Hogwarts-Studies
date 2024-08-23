from flask import Flask, request
from werkzeug.utils import secure_filename

# 创建 Flask 应用程序实例
API = Flask(__name__)


@API.route('/gettoken')
def get_token():
    """一般用于获取url后面的参数，返回token鉴权等"""
    # 获取 URL 中的请求参数
    url_param = request.args
    # 查看获取到的请求参数的类型
    print(type(url_param))
    # 获取请求参数中的 username 对应的值
    username = url_param.get('username')
    password = url_param.get('password')
    return f'Hello, {(username, password)}!'


@API.route('/data', methods=['POST'])
def process_data():
    # 获取 JSON 格式请求体
    data = request.json
    # 查看获取到的请求参数的类型
    print(type(data))
    # 获取请求体中对应字段的值
    name = data.get('name')
    age = data.get('age')
    return f'Name: {name}, Age: {age}'


@API.route('/login', methods=['POST'])
def login():
    # 获取表单格式请求体
    user_info = request.form
    # 查看获取到的请求参数的类型
    print(type(user_info))
    # 获取请求体中对应字段的值
    username = user_info.get('username')
    password = user_info.get('password')
    return f'Welcome, {username}!'


@API.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # 获取请求 URL
    r_url = request.url
    # 获取请求域名
    r_host = request.host
    # 获取请求头信息
    r_headers = request.headers
    # 获取请求方法
    r_method = request.method
    print(f"Url:{r_url}\nHost:{r_host}\nHeaders:\n{r_headers}")
    # 获取文件请求体
    r_file = request.files
    # 判断请求方法为 POST
    if r_method == 'POST':
        # 判断请求头中包含 My-Header 字段并且值为 hogwarts
        if r_headers.get('My-Header') == "hogwarts":
            # 保存文件
            f = r_file.get("file")
            f.save('./' + secure_filename(f.filename))
            return f'File {f.filename} is saved! URL is {r_url}, host is {r_host}'
        return f"My-Header is missing!"
    elif r_method == 'GET':
        return f"Please send POST method and upload file."


# 运行应用程序
if __name__ == '__main__':
    API.run()
