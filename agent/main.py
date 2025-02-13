import uvicorn, os

from init import create_app

app = create_app()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=os.environ.get('APP_HOST', '0.0.0.0'),
        port=int(os.environ.get('APP_PORT', 8000)),
        reload=bool(os.environ.get('APP_DEBUG'))
    )