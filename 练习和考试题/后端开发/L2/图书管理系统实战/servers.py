from flask import Flask
from flask_cors import CORS

from BookBP import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 注册蓝图
app.register_blueprint(bookBP)
app.run(debug=True, port=8888)
