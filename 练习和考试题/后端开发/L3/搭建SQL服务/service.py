from flask import Flask, request

app = Flask(__name__)


@app.route('/mysql', methods=['POST'])
def use_mysql_serve():
    json_data = request.form
    sql_str = json_data.get('sql')
    from sql import sql_parse_demo
    return sql_parse_demo(sql=sql_str).rule()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
