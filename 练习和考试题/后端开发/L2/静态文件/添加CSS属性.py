from flask import Flask, render_template

# 创建 Flask 应用程序实例
app = Flask(__name__)


# 定义路由和视图函数
@app.route("/")
def show_static():
    return render_template("static3.html")


"""
首先创建static/style.css文件
在html中添加引用
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
  </head>
  
并给img添加class属性
img
        alt="branch"
        class="hogwarts"
        src="{{ url_for('static', filename='images/branch.jpg') }}"
      />
"""
# 运行应用程序
if __name__ == '__main__':
    app.run(debug=True, port=5050)
