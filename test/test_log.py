'''
@file: test_log.py
@brief: 测试 py_assist.log 模块的功能
@details: pytest test/test_log.py
@date: 2025-05-11
@author: Yuru.Tu <ccl70710@gmail.com>
@copyright: (c) 2025 Yuru.Tu. All rights reserved.
'''
import threading
import pytest
import logging

from py_assist.log import LoggerSingleton
from py_assist.pattern.singleton import SingletonType

def test_same_instance_with_same_name():
    """
    同一个名称多次实例化应该返回同一个对象
    """
    logger1 = LoggerSingleton("app")
    logger2 = LoggerSingleton("app")
    assert logger1 is logger2, "多次用相同 name 实例化，应返回同一个实例"


def test_same_instance_with_different_name():
    """
    不同名称参数也只会创建一次实例，后续忽略 new name
    """
    # 清理已有实例
    SingletonType.clear_instances(LoggerSingleton)

    logger1 = LoggerSingleton("first_name")
    logger2 = LoggerSingleton("second_name")
    assert logger1 is logger2, "不同 name 也应返回同一个实例"
    # 名称只在第一次初始化时生效
    underlying = logger1.get_underlying()
    assert underlying.name == "first_name"


def test_handler_configured_only_once(tmp_path, caplog):
    """
    验证 handler 只会被添加一次，避免重复输出
    """
    # 清理已有 handlers
    inst = LoggerSingleton("test")
    underlying = inst.get_underlying()
    # 模拟再调用一次 __init__（尽管不会再次添加 handler）
    LoggerSingleton("ignored")
    # 断言 handlers 只有一个
    assert len(underlying.handlers) == 1

    # 测试实际输出
    caplog.set_level(logging.INFO)
    underlying.info("hello")
    assert "hello" in caplog.text


def test_thread_safety_of_singleton():
    """
    多线程并发取实例，应拿到同一个对象
    """
    instances = [None] * 10
    def worker(idx):
        instances[idx] = LoggerSingleton("concurrent")

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(len(instances))]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # 确保所有线程拿到的都是同一个实例
    first = instances[0]
    for inst in instances[1:]:
        assert inst is first
