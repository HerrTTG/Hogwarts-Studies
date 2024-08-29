from sqlalchemy import create_engine

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
