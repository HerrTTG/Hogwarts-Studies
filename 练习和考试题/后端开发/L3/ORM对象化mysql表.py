from pydantic import BaseModel, ConfigDict, constr
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import Optional

# 声明基类
Base = declarative_base()

# 申明数据库信息
# mysql 登录用户名
username = "root"
# mysql 登录密码
pwd = "Kuoka314+"
# mysql 域名
host = "127.0.0.1"
# mysql 端口
port = 3306
# 要操作的数据库名
database = "hogwarts"
# 创建引擎
engine = create_engine(f"mysql+pymysql://{username}:{pwd}@{host}:{port}/{database}")


# 定义表结构
class Course(Base):
    """这个类到底是指向数据库还是表对象？换句话问，这个类是否可以承担创建多个表的工作。"""

    __tablename__ = "t_course"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    detail = Column(String(255), default="")


class CourseModel(BaseModel):
    # 允许通过其他类实例来生成并初始化一个 Pydantic 实例
    model_config = ConfigDict(from_attributes=True)

    # id 属性为整型
    id: int
    # name 属性为字符串，最大长度为 30
    name: constr(max_length=30)
    # Optional 的作用是可选类型，告诉 IDE 或者框架这个参数除了给定的默认值外还可以是 None
    detail: Optional[constr(max_length=255)] = ""


if __name__ == '__main__':
    # 数据库初始化创建表
    Course.metadata.create_all(engine)

    # 创建会话
    DBSession = sessionmaker(bind=engine)
    # 获取会话实例
    db_session = DBSession()

    # 查询
    course_data = db_session.query(Course).filter_by(id=1).first()

    # 使用 pydantic 把结果转为 pydantic 对象，并校验其结构。无误后把查询结果对象转为字典格式。
    datas = CourseModel.model_validate(course_data).model_dump()
    print(datas)
    # 关闭连接
    db_session.close()
