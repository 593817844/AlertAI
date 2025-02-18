import logging, os
from logging import handlers, Logger


def getLogger(name: str='root') -> Logger:
    """
    创建一个日志器的单例对象
    :param name: 日期器名字，默认为root
    :return: 日志器对象
    :return:
    """
    # 1、创建一个logger日期器对象
    logger: Logger = logging.getLogger(name)
    # 2、设置下logger的日志的等级
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        # 3、创建合适的Handler(FileHandler要有保存路径)
        th: logging.StreamHandler = logging.StreamHandler()  # 终端处理器
        try:
            # 创建日志目录
            os.mkdir("logs")
        except:
            pass
        rf: handlers.RotatingFileHandler = handlers.RotatingFileHandler(  # 按文件大小分割日志
            filename=f"logs/{name}.log", # 日志文件名，日志目录log需要手动创建
            mode='a',  # a=append 追加写入
            maxBytes=300*1024*1024,  # 单个日志文件大小的最大值
            backupCount=10,  # 备份日志文件的数量，所有日志数量 = backupCount+filename
            encoding='utf-8' # 日志文件内容的编码
        )
        # 4、设置下每个Handler的日志等级【Handler的日志等级会覆盖上面logger的日志的等级】
        th.setLevel(logging.DEBUG)
        rf.setLevel(logging.INFO)

        # 5、创建下日志的格式器对象formatter
        simple_formatter: logging.Formatter = logging.Formatter(
            fmt="{levelname} {asctime} {pathname}:{lineno} {message}",
            style="{"
        )
        verbose_formatter: logging.Formatter = logging.Formatter(
            fmt="【{name}】{levelname} {asctime} {pathname}:{lineno} {message}",
            datefmt="%Y-%m-%d %H:%M:%S",
            style="{"
        )

        # 6、向Handler中添加上面创建的格式器对象
        th.setFormatter(simple_formatter)
        rf.setFormatter(verbose_formatter)

        # 7、将上面创建的Handler处理器添加到logger日志器中
        logger.addHandler(th)
        logger.addHandler(rf)

    return logger


if __name__ == '__main__':
    logger = getLogger('dl')
    logger.info("这里是常规运行日志")
    logger.debug("开发人员在调试程序时自己手动打印的日志")
    logger.warning("这里是程序遇到未来会废弃的函数/方法时，输出的警告日志")
    logger.error("这里是程序发生错误时输出的日志")
    logger.critical("这是致命级别的日志，需要紧急修复的")

    # 多次调用实例化出来的日志对象，如果name相同，则得到的是同一个日志器对象（单例模式）
    logger1 = getLogger('dl')
    print(id(logger1), id(logger))
