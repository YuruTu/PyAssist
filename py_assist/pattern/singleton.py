'''
@file: singleton.py
@brief: This module implements the Singleton design pattern using a metaclass.
@date: 2025-05-11
@author: Yuru.Tu <ccl70710@gmail.com>
@copyright: (c) 2025 Yuru.Tu. All rights reserved.
'''
class SingletonType(type):
    """
    Metaclass used to create a singleton.
    When a class is instantiated using this metaclass,
    it first checks if an instance already exists and returns it if so.
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # 第一次创建实例
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

    @classmethod
    def clear_instances(mcs, target_cls=None):
        """
        Clear the singleton state.
        If target_cls is provided, only clear the instance for that class;
        otherwise, clear all stored instances.
        """
        if target_cls is not None:
            mcs._instances.pop(target_cls, None)
        else:
            mcs._instances.clear()
