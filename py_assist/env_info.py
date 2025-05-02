"""
@file: env_info.py
@brief: This script prints the current environment information, including the Python version.
@date: 2025-05-03
@author: Yuru.Tu
@copyright: (c) 2025 Yuru.Tu. All rights reserved.
"""
import logging
import sys
from importlib.metadata import version, PackageNotFoundError

def print_package_info(package_name):
    try:
        package_version = version(package_name)
        logging.info(f'{package_name} version: {package_version}')
    except PackageNotFoundError:
        logging.error(f'{package_name} is not installed')

def print_env_info(package_list=[]):
    """
    Prints the current environment information, including Python version and specified packages.
    :param package_list: List of package names to check versions for.
    """
    logging.info(f"Python version: {sys.version}")
    logging.info(f"Python executable: {sys.executable}")
    for package in package_list:
        print_package_info(package)
