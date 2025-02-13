import os
from fastapi import FastAPI
from dotenv import load_dotenv
from apps.alerts.views import app as alert_app
from utils import middleware

def create_app() -> FastAPI:
    """工厂函数：创建App对象"""
    # 读取环境配置文件的信息，加载到环境变量
    load_dotenv()

    app = FastAPI(
        title=os.environ.get('APP_NAME'),
        summary=os.environ.get('APP_SUMMARY'),
        description=os.environ.get('APP_DESCRIPTION'),
        version=os.environ.get('APP_VERSION'),
    )

    # 注册各个分组应用中的视图接口代码到App应用对象中
    app.include_router(alert_app)
    # app.include_router(alert_app, prefix='/alertmamager')  # prefix url路径前缀，

    # 注册中间件函数
    http_middleware = app.middleware('http')
    http_middleware(middleware.log_requests)

    return app
