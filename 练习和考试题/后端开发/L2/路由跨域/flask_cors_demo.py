# 后端服务代码
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return render_template("cors.html")


if __name__ == '__main__':
    app.run(debug=True, port=5055)
