from starlette.middleware.base import BaseHTTPMiddleware
class TimmerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print('请求来了2')
        # 这里的代码就是请求处理前的逻辑
        response = await call_next(request) #意思是处理完请求报文后，继续交给下一个中间件去处理
        # 这里的代码就是请求处理后的逻辑
        print('响应回去了2')
        return response  