from fastapi import APIRouter, Depends, Path

from database.db import Session, get_db
from exception.custorm_exception import CustormException
from model.student import ReturnStudentModel, StudentAddModel, StudentUpdateModel
from service.student import add_student_service, delete_student_service, get_student_list_service, get_student_srevice, update_student_service
from utils.r import R
#prefix是当前模块接口路径中的公共前缀，这里配了后面接口装饰器中的路径就可不写了
#tag是接口文档的分组，根据功能进行分组，方便查看
student_router=APIRouter(prefix="/student",tags=["学生管理"])

@student_router.post('/')
def add_student(student_info: StudentAddModel, session: Session = Depends(get_db)):
  #依赖函数必须传递函数，依赖类会根据参数类型去找对应的类实例化，但是函数不行，必须得传递
# #     1、考虑把student_info对象转换成学生对象
# #     后期我们不会把这些收到参数要转化等逻辑写在这里，而是创建service，放到service中去处理这些逻辑
# #     2、保存到数据库中
# #     保存数据库的操作，我们是在service当中处理完，然后把处理好的数据，再传递给另外一个crud专门去操作数据库
  add_student_service(student_info,session)
  return R()
  
@student_router.put('/')
def update_student(student_info: StudentUpdateModel,session: Session = Depends(get_db)):
  # 除0异常测试
  # a = 10 / 0
  
  # 文件找不到异常
  # f = open("askdhaksdj",'r')

  # 列表越界异常
  # list1 = [1,2,3]
  # print(list1[4])

  # 库存不足
  # count = 5
  # if count > 4:
  #     # 抛异常，没有异常，就自定义异常去抛
  #     raise CustormException(code=1001,msg="库存不足")

  # 用户名不对
  # username = "zhaoliying"
  # if username != "yangmi":
  #     raise CustormException(code=1002,msg="用户名不对")  
  
  
  update_student_service(student_info,session)
  return R()

@student_router.delete('/{id}')
def delete_student(id:int,session: Session = Depends(get_db)):
  delete_student_service(id,session)
  return R()

@student_router.get("/{id}",summary="查询单个学生信息",response_description="成功返回学生的详细信息")
def get_student(
    id: int = Path(..., description="要查询的学生ID"),
    session: Session = Depends(get_db)):
  print("接口执行了")
  student=get_student_srevice(id,session)
  # 现在返回的数据是要经过脱敏，此时我们就可以使用返回值的模型类从student对象当中获取模型类里面有的属性
  
  result = ReturnStudentModel.from_orm(student)
  return R(data=result)


@student_router.get('/')
def get_student_list(session: Session = Depends(get_db)):
  student_list=get_student_list_service(session)
  result = [ReturnStudentModel.from_orm(student) for student in student_list]
  return R(data=result)

