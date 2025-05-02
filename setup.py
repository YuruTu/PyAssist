'''
@file: setup.py
@brief: This script sets up the package for distribution using setuptools.
@details: It includes metadata such as name, version, author, and dependencies.
@author: Yuru.Tu
@date: 2025-05-03
@copyright: (c) 2025 Yuru.Tu. All rights reserved.
'''
from setuptools import setup, find_packages

setup(
    name='py_assist',  # 包的名字
    version='0.0.1',  # 包的版本
    packages=find_packages(),  # 自动寻找当前目录下所有的包
    install_requires=[  # 项目的依赖包
        # 'pandas',
    ],
    # 如果有命令行工具，可以这样配置
    # entry_points={
    #     'console_scripts': [
    #         'your_command = your_package_name.module:main_function',
    #     ],
    # },
    # 包的其它元数据
    author='Yuru.Tu',
    author_email='ccl70710@gmail.com',
    description='A short description of the package',
    long_description=open('README.md').read(),  # 长描述来自 README 文件
    # long_description_content_type='text/markdown',  # 如果你用了 markdown 格式
    url='https://github.com/YuruTu/PyAssist',  # 项目的 GitHub 地址
    classifiers=[  # 分类器列表，帮助 PyPI 分类
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # 需要 Python 版本
)
