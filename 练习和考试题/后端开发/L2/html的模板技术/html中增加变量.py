from flask import Flask, Blueprint, render_template

app = Flask(__name__)
index_home = Blueprint(name='home', url_prefix="/home", import_name=__name__)


@index_home.route("")
def home_page():
    return render_template("home1.html", name="haizhenyu")


if __name__ == "__main__":
    app.register_blueprint(index_home)
    app.run("0.0.0.0", debug=True, port=5050)
