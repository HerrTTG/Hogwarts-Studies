from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# 创建 Flask 应用程序实例
app = Flask(__name__)
Bootstrap(app)


# 定义路由和视图函数
@app.route("/")
def index():
    return render_template("bootstrap_index.html")


# 运行应用程序
if __name__ == '__main__':
    app.run(debug=True, port=5055)
