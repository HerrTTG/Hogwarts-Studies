from flask import Flask, render_template

# 创建 Flask 应用程序实例
app = Flask(__name__)


@app.route("/extend")
def extend():
    return render_template("son.html")


# 运行应用程序
if __name__ == '__main__':
    app.run("0.0.0.0", port=5055, debug=True)
