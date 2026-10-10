from database.db import Base
from sqlalchemy import Column ,Integer ,String, Date
from pydantic import BaseModel, Field

class Student(Base):
  __tablename__ ='student'
  id = Column(Integer,primary_key=True,autoincrement=True,comment="主键id")
  name=Column(String(50),nullable=False,comment='学生姓名')
  age=Column(Integer,default=18,comment="学生年龄")
  birthday=Column(Date,comment="学生生日")

class StudentAddModel(BaseModel):
  name:str =Field(...,description="学生姓名")
  age:int =Field(default=18,description="学生年龄")
  birthday:str =Field(description="学生生日")

class StudentUpdateModel(BaseModel):
  id:int =Field(...,escription="学生id")
  name:str =Field(...,description="学生姓名")
  age:int =Field(default=18,description="学生年龄")
  birthday:str =Field(description="学生生日")


# 专门定义一个返回数据的模型类，里面把不需要的敏感的信息给去掉了
class ReturnStudentModel(BaseModel):
  id:int=Field(...,description="学生id")
  name:str=Field(...,description="学生姓名")    
  # 允许模型类直接从学生对象当中获取同名的属性组成新的对象
  class Config:
    from_attributes=True