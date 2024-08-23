from flask import Flask, render_template

# 创建 Flask 应用程序实例
app = Flask(__name__)


# 定义路由和视图函数
@app.route("/")
def show_static():
    return render_template("static2.html")


"""
  <img
        alt="Gryffindor"
        src="{{ url_for('static', filename='images/Gryffindor.jpg') }}"
      />
"""

# 运行应用程序
if __name__ == '__main__':
    app.run(debug=True, port=5050)
