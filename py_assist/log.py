"""
@file: log.py
@brief: This script configures the logging settings for the application.
@details: It sets up a logger that outputs logs to both the console and a file.
@date: 2025-05-03
@author: Yuru.Tu
@copyright: (c) 2025 Yuru.Tu. All rights reserved.
"""
import logging
from py_assist.pattern.singleton import SingletonType

# 配置日志
def setup_logging(log_file='app.log'):
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # 设置日志级别为 DEBUG，包含所有级别的日志（DEBUG, INFO, WARNING, ERROR, CRITICAL）

    # 创建格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 创建控制台处理器（输出到屏幕）
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # 控制台日志级别为 DEBUG
    console_handler.setFormatter(formatter)

    # 创建文件处理器（输出到文件）
    file_handler = logging.FileHandler(log_file,mode='w',encoding='utf-8')
    file_handler.setLevel(logging.INFO)  # 文件日志级别为 INFO，只记录 INFO 及以上级别的日志
    file_handler.setFormatter(formatter)

    # 将处理器添加到日志器中
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

class LoggerSingleton(metaclass=SingletonType):
    """
    Singleton logger class. It configures the Handler/Formatter only once during initialization.
    Subsequent calls return the same underlying Logger object.
    """
    def __init__(self, name: str = __name__):
        # Retrieve or create a named Logger
        self._logger = logging.getLogger(name)
        # Add a handler only on first construction to avoid duplicate outputs
        if not self._logger.handlers:
            self._logger.setLevel(logging.INFO)
            ch = logging.StreamHandler()
            fmt = logging.Formatter("%(asctime)s %(name)s [%(levelname)s] %(message)s")
            ch.setFormatter(fmt)
            self._logger.addHandler(ch)

    # Expose common logging methods
    def debug(self, msg, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        self._logger.exception(msg, *args, **kwargs)

    def get_underlying(self) -> logging.Logger:
        """Returns the native Logger object if direct access is needed."""
        return self._logger
