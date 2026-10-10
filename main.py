from fastapi import  FastAPI
from fastapi.exceptions import RequestValidationError
from exception.custorm_exception import CustormException
from exception.handler import custorm_exception_error_handler, exception_handler, file_not_found_error_handler, request_value_error_handler, zero_division_error_handler
from middleware.logger_middleware import LoggerMiddleware
from middleware.timmer_middleware import TimmerMiddleware
from router.student import student_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn



from database.db import Base,engine
app = FastAPI(
  title="学生管理器",
  description = "学生管理器后端接口",
  version= "0.1.0"
)

app.include_router(student_router,prefix="/api/v1")

# 把创建好的异常处理器都得添加给app应用
app.add_exception_handler(ZeroDivisionError,zero_division_error_handler)
app.add_exception_handler(FileNotFoundError,file_not_found_error_handler)
app.add_exception_handler(CustormException,custorm_exception_error_handler)
app.add_exception_handler(Exception,exception_handler)

# 参数校验异常处理器的添加 其实框架已经处理过了，我们在这自己处理，会覆盖框架的处理器
app.add_exception_handler(RequestValidationError,request_value_error_handler)


# 添加中间件（注册中间件） 注册中间件的顺序决定了后期哪个中间件先走，越靠后注册，越靠前走
app.add_middleware(TimmerMiddleware)
app.add_middleware(LoggerMiddleware)

# 配置跨域的内置中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源（生产环境需指定具体域名）
    allow_credentials=True, #允许将凭据包含在跨域请求中
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有请求头
)

@app.get('/')
def index():
  return {'msg':'hello world'}


# @app.post('/student')
# def add_student(student_info: StudentAddModel, session: Session = Depends(get_db)):
#   #依赖函数必须传递函数，依赖类会根据参数类型去找对应的类实例化，但是函数不行，必须得传递
# # #     1、考虑把student_info对象转换成学生对象
# # #     后期我们不会把这些收到参数要转化等逻辑写在这里，而是创建service，放到service中去处理这些逻辑
# # #     2、保存到数据库中
# # #     保存数据库的操作，我们是在service当中处理完，然后把处理好的数据，再传递给另外一个crud专门去操作数据库
#   add_student_service(student_info,session)
#   return R()
  
# @app.put('/student')
# def update_student(student_info: StudentUpdateModel,session: Session = Depends(get_db)):
#   update_student_service(student_info,session)
#   return R()

# @app.delete('/student/{id}')
# def delete_student(id:int,session: Session = Depends(get_db)):
#   delete_student_service(id,session)
#   return R()

# @app.get('/student/{id}')
# def get_student(id:int,session: Session = Depends(get_db)):
#   student=get_student_srevice(id,session)
#   return R(data=student)

# @app.get('/student')
# def get_student_list(session: Session = Depends(get_db)):
#   student_list=get_student_list_service(session)
#   return R(data=student_list)


if __name__ == '__main__' :
  Base.metadata.create_all(bind=engine) #根据所有继承 Base 的模型定义，在 engine 指向的数据库里，创建所有不存在的表。适合开发阶段初始化数据库，生产环境改表用 Alembic。
  uvicorn.run(
    "main:app",   #指定启用的模块（主文件）和对象
    host='0.0.0.0',
    port=8000,
    reload=True
  )  


  
  