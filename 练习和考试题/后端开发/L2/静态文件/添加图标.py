from flask import Flask, render_template

# 创建 Flask 应用程序实例
app = Flask(__name__)


# 定义路由和视图函数
@app.route("/")
def show_static():
    return render_template("static1.html")


"""
假如在 static 文件夹的根目录下面放了一个 logo.jpg 文件，可以这样来获取图片并添加为图标：
 <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>静态文件</title>
    <link rel="icon" href="{{ url_for('static', filename='logo.jpg') }}" />
  </head>
添加进html
"""

# 运行应用程序
if __name__ == '__main__':
    app.run(debug=True, port=5050)
