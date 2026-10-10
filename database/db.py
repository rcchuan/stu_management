from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base #db.py从sqlalchemy导入的sessionmaker是用来创建操作数据库的会话的，从sqlalchemy导入的declarative_base通过Base类这个’中间人‘是用来把 Python 类映射到数据库表的。
import os

#设置DATABASE_URL环境变量
#powershell设置：$env:DATABASE_URL = "mysql+pymysql://用户名:密码@数据库地址:3306/数据库名"
#bash设置：export DATABASE_URL='mysql+pymysql://用户名:密码@数据库地址:3306/数据库名'
#cmd设置：set "DATABASE_URL=mysql+pymysql://用户名:密码@数据库地址:3306/数据库名"
engine = create_engine(os.environ["DATABASE_URL"])

# engine = create_engine("mysql+pymysql://root:123456@192.168.100.102:3306/test")
Base = declarative_base()
Session = sessionmaker(bind=engine)

#写依赖函数生成session对象
#把生成器函数当依赖使用，调用函数返回生成器，内部调用next方法获得session对象
def get_db():
  session=Session()
  try:
      yield session
  finally:
     session.close()
  