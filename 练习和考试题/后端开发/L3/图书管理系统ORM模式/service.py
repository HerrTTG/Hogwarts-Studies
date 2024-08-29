import json
import sqlalchemy
from flask import Flask, Blueprint, request
from pydantic import ValidationError

from DBsession import db_session
from Database import Course, CourseModel

app = Flask(__name__)
CourseBlue = Blueprint(name="Course", import_name='__name__', url_prefix='/course')


@CourseBlue.route("", methods=['GET'])
def get():
    url_param = request.args
    try:
        id = int(url_param.get("id"))
        course_data = db_session.query(Course).filter_by(id=id).first()
        if course_data is None:
            return json.dumps({
                "errcode": 10001,
                "errmsg": "课程不存在"
            }, ensure_ascii=False)
        else:
            data = CourseModel.model_validate(course_data).model_dump()

    except ValidationError as ove:
        return json.dumps({
            "errcode": 10003,
            # 通过 e.errors() 获取错误列表
            # repr 为内置函数，返回一个对象的 string 格式
            "errmsg": "内部数据错误，不符合规则"
        }, ensure_ascii=False)

    except ValueError as ve:
        return json.dumps({
            "errcode": 10002,
            # 通过 e.errors() 获取错误列表
            # repr 为内置函数，返回一个对象的 string 格式
            "errmsg": "输入数据不符合规则"
        }, ensure_ascii=False)


    except Exception as e:
        return json.dumps({
            "errcode": 10009,
            "errmsg": "服务出现错误"
        }, ensure_ascii=False)

    else:
        db_session.close()
        return json.dumps({"errcode": 0,
                           "errmsg": "获取课程成功！",
                           "data": data}, ensure_ascii=False)


@CourseBlue.route("/list", methods=['GET'])
def list():
    try:
        course_datas = db_session.query(Course).all()
        if course_datas is None:
            return json.dumps({
                "errcode": 10001,
                "errmsg": "课程不存在"
            }, ensure_ascii=False)
        datas = [CourseModel.model_validate(item).model_dump() for item in course_datas]
        db_session.close()

    except ValidationError as ove:
        return json.dumps({
            "errcode": 10003,
            # 通过 e.errors() 获取错误列表
            # repr 为内置函数，返回一个对象的 string 格式
            "errmsg": "内部数据错误，不符合规则"
        }, ensure_ascii=False)

    except Exception as e:

        return json.dumps({

            "errcode": 10009,

            "errmsg": "服务出现错误"

        }, ensure_ascii=False)

    else:
        return json.dumps({
            "errcode": 0,
            "errmsg": "获取全部课程列表成功！",
            "datas": datas
        }, ensure_ascii=False)


@CourseBlue.route("", methods=["PUT"])
def update_course():
    request_args = request.get_json()
    try:
        # 使用 pydantic 把请求参数转为 pydantic 对象
        CourseModel.model_validate(request_args)
    except ValidationError as e:
        print(e)
        return {
            "errcode": 10002,
            "errmsg": repr(e.errors())
        }

    # 构造orm对象
    course_data = Course(**request_args)
    # 根据课程 id 进行查询，如果查找不到结果则返回课程不存在
    if db_session.query(Course).filter_by(id=course_data.id).first() is None:
        return json.dumps({
            "errcode": 10001,
            "errmsg": "课程不存在"
        }, ensure_ascii=False)

    # 使用 pydantic 把请求数据转为字典
    data = CourseModel.model_validate(request_args).model_dump()
    # 更新数据
    db_session.query(Course).filter_by(id=course_data.id).update(data)
    # 提交操作
    db_session.commit()
    # 关闭连接
    db_session.close()
    return json.dumps({
        "errcode": 0,
        "errmsg": "课程修改成功"
    }, ensure_ascii=False)


@CourseBlue.route("", methods=["POST"])
def add():
    request_args = request.get_json()
    try:
        # 使用 pydantic 把请求参数转为 pydantic 对象
        data = CourseModel.model_validate(request_args).model_dump()
    except ValidationError as e:
        print(e)
        return {
            "errcode": 10002,
            "errmsg": repr(e.errors())
        }

    try:
        # 添加数据
        db_session.add(Course(**data))
        # 提交操作
        db_session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        db_session.close()
        return e
    except sqlalchemy.exc.PendingRollbackError as a:
        db_session.close()
        return a
    except Exception:
        db_session.close()
    else:
        # 关闭连接
        db_session.close()
        return json.dumps({
            "errcode": 0,
            "errmsg": "课程添加成功"
        }, ensure_ascii=False)


@CourseBlue.route(f"/<int:course_id>", methods=["DELETE"])
def delete(course_id):
    course_data = db_session.query(Course).filter(Course.id == course_id).first()
    if course_data is None:
        return json.dumps({
            "errcode": 10001,
            "errmsg": "课程不存在"
        }, ensure_ascii=False)
    try:
        # 删除查找到的课程
        db_session.delete(course_data)
        # 提交操作
        db_session.commit()
    except Exception as e:
        # 关闭连接
        db_session.close()
    else:
        return json.dumps({
            "errcode": 0,
            "errmsg": "课程删除成功"
        }, ensure_ascii=False)


if __name__ == "__main__":
    app.register_blueprint(CourseBlue)
    app.run("0.0.0.0", port=8888, debug=True)
