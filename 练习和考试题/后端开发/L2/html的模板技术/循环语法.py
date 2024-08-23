from flask import Flask, Blueprint, render_template

app = Flask(__name__)
index_people = Blueprint(name="people", import_name=__name__, url_prefix="/people")


@index_people.route("")
def people_page():
    people = [
        {
            "name": "lily",
            "age": 18,
            "gender": "female"
        },
        {
            "name": "tom",
            "age": 19,
            "gender": "male"
        },
    ]
    return render_template("people.html", people=people)


if __name__ == "__main__":
    app.register_blueprint(index_people)
    app.run("0.0.0.0", debug=True, port=5050)
