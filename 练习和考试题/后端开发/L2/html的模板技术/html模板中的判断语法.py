from flask import Flask, Blueprint, render_template

app = Flask(__name__)
index_home = Blueprint(name='home', import_name=__name__, url_prefix="/home")


@index_home.route("")
def home_page():
    person = {
        "name": "lily",
        "age": 18,
        "gender": "female"
    }

    return render_template("home2.html", person=person)


if __name__ == "__main__":
    app.register_blueprint(index_home)
    app.run("0.0.0.0", port=5050, debug=True)
