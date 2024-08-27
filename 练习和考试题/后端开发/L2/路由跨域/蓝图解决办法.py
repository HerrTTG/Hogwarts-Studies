from flask import Flask, Blueprint, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# 第一种：全局解决跨域问题
CORS(app, supports_credentials=True)

hello_route = Blueprint("hello", __name__, url_prefix="/hello")


# 第二种：局部解决跨域问题
@cross_origin(supports_credentials=True)
@hello_route.route("")
def hello():
    return render_template("cors.html")


if __name__ == '__main__':
    app.register_blueprint(hello_route)
    app.run(debug=True, port=5555)
