from starlette.middleware.base import BaseHTTPMiddleware
class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print('请求来了1')
        # 这里的代码就是请求处理前的逻辑
        response = await call_next(request) #意思是处理完请求报文后，继续交给下一个中间件去处理
        # 这里的代码就是请求处理后的逻辑
        print('响应回去了1')
        return response  
# 中间件是可以对任何接口进行添加功能，而装饰器是针对某个接口添加功能，粒度不一样
# 后期假设你只是想对某个功能添加那么就用装饰器，如果想对所有接口都添加那么就用中间件