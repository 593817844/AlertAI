import os

TORTOISE_ORM = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.mysql',  # MySQL or Mariadb
            'credentials': {  # 连接参数
                'host': os.environ.get('DB_HOST', '127.0.0.1'),  # 数据库IP/域名地址
                'port': int(os.environ.get('DB_PORT', 3306)),  # 端口
                'user': os.environ.get('DB_USER', 'root'),  # 连接账户
                'password': os.environ.get('DB_PASSWORD', '123'),  # 连接密码
                'database': os.environ.get('DB_DATABASE', 'alert'),  # 数据库
                'charset': os.environ.get('DB_CHARSET', 'utf8mb4'),  # 编码
                'minsize': int(os.environ.get('DB_POOL_MINSIZE', 1)),  # 连接池中的最小连接数
                'maxsize': int(os.environ.get('DB_POOL_MAXSIZE', 5)),  # 连接池中的最大连接数
                "echo": bool(os.environ.get('DEBUG', True))  # 执行数据库操作时，是否打印SQL语句
            }
        }
    },
    'apps': {  # 默认所在的应用目录
        'models': {  # 数据模型的分组名
            # 'models': ['applicaton.apps.users.models', 'aerich.models'],  # 模型所在目录文件的导包路径[字符串格式]
            'models': ['apps.alerts.models','apps.systeminfo.models','apps.users.models'],
            'default_connection': 'default',  # 上一行配置中的模型列表的默认连接配置
        }
    },
    # 时区设置
    # 当use_tz=True，当前tortoise-orm会默认使用当前程序所在操作系统的时区，
    # 当use_tz=False时，当前tortoise-orm会默认使用timezone配置项中的时区
    'use_tz': False,
    'timezone': os.environ.get('APP_TIMEZONE', 'Asia/Shanghai')
}


REDIS = {
    'host': os.environ.get('RD_HOST', '127.0.0.1'), # 数据库地址
    'port': os.environ.get('RD_PORT', 6379),        # 数据库端口
    'db': os.environ.get('RD_DB', 0),               # 数据库名
    'username':  os.environ.get('RD_USERNAME', ''), # 用户名
    'password':  os.environ.get('RD_PASSWORD', ''), # 密码
}

JWT = {
    # 秘钥[盐值]
    'secret_key': os.environ.get('APP_SECRET', 'sp$dto8.cO*zNe@gkntwYb2B0DBflnShlQbA96wdLA.V9J38JyV1FdindI6Oh7s4'),
    # 设定JWT令牌签名算法
    'algorithm': "HS256",
    # 设置令牌过期时间变量（单位：秒）
    'expire_time': 30 * 60
}