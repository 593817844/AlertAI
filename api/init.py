import os
from fastapi import FastAPI
from dotenv import load_dotenv
from tortoise.contrib.fastapi import register_tortoise
from apps.alerts.views import app as alert_app
from apps.systeminfo.views import app as system_app
from apps.ai.views import app as ai_app
from apps.users.views import app as user_app
import settings
from utils import middleware,exceptions
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    """工厂函数：创建App对象"""
    # 读取环境配置文件的信息，加载到环境变量
    load_dotenv()

    app = FastAPI(
        title=os.environ.get('APP_NAME'),
        summary=os.environ.get('APP_SUMMARY'),
        description=os.environ.get('APP_DESCRIPTION'),
        version=os.environ.get('APP_VERSION'),
        # 注册全局异常处理函数
        exception_handlers={
            exceptions.HTTPException: exceptions.global_http_exception_handler,
            exceptions.RequestValidationError: exceptions.global_request_exception_handler,
        }
    )

    # 允许跨域的来源，可以设置为前端的 URL 地址
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 这里设置为前端地址，如果前端是用 React/Vue 的开发服务器，通常是 http://localhost:3000
        allow_credentials=True,
        allow_methods=["*"],  # 允许所有 HTTP 方法
        allow_headers=["*"],  # 允许所有请求头
    )

    # 把tortoise-orm注册到App应用对象中
    register_tortoise(
        app,
        config=settings.TORTOISE_ORM,
        generate_schemas=False,  # 是否自动生成表结构[自动根据配置项中apps.models的路径自动识别模型]
        add_exception_handlers=True,  # 是否启用自动异常处理
    )

    # redis连接对象注册到App应用对象中
    # redis_tools.register_redis(
    #     app,
    #     config=settings.REDIS,
    # )

    # 注册各个分组应用中的视图接口代码到App应用对象中
    app.include_router(alert_app)
    app.include_router(system_app)
    app.include_router(ai_app)
    app.include_router(user_app)
    # app.include_router(alert_app, prefix='/alertmamager')  # prefix url路径前缀，

    # 注册中间件函数
    http_middleware = app.middleware('http')
    http_middleware(middleware.log_requests)

    return app
