from pydantic import BaseModel, ConfigDict, constr
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from typing import Optional

Base = declarative_base()


class Course(Base):
    """一个类就是一个表"""

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
