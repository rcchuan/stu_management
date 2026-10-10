#该文件是专门用于异常处理的异常处理器

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.requests import Request

from exception.custorm_exception import CustormException
from utils.r import R


# 1、为特定异常定义一个异常处理器（函数）
# 2、在应用app当中添加上这个异常处理器
# 除0异常的处理器
def zero_division_error_handler(request:Request,exception:ZeroDivisionError):
  print(exception)
  # 下面这行代码切记，json必须得自己转化，因为不是接口主函数
  return JSONResponse(R(code=500,msg=f"除零错误{exception}").__dict__)

def file_not_found_error_handler(request:Request,exception:FileNotFoundError):
  print(exception)
  # 下面这行代码切记，json必须得自己转化，因为不是接口主函数
  return JSONResponse(R(code=404,msg=f"文件资源不存在{exception}").__dict__)

# 自定义异常处理器
def custorm_exception_error_handler(request: Request,exception: CustormException):
    # exception： 代表就是异常对象
    print(exception)
    return JSONResponse(R(code=exception.code, msg=exception.msg).__dict__)


#参数校验异常
def request_value_error_handler(request: Request,exception:RequestValidationError):
  print(exception.errors)
  # 整理错误的信息，放到data中
  data={}
  for error in exception.errors():
     key=error["loc"][-1]
     value=error["msg"]
     data[key]=value 
  return JSONResponse(R(code=500, msg=f"参数校验异常",data=data).__dict__)


# 异常兜底
def exception_handler(request: Request, exception: Exception):
    print(exception)
    return JSONResponse(R(code=500, msg=f"未知异常{exception}").__dict__)