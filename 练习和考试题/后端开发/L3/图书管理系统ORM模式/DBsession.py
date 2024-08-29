from sqlalchemy.orm import sessionmaker

from Database import Course
from configs import engine

Course.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
# 获取会话实例
db_session = DBSession()
