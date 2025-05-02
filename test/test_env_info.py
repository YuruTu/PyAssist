import sys
import logging
from py_assist.env_info import print_env_info
from py_assist.log import setup_logging

if __name__ == "__main__":
    setup_logging(sys.argv[0] + ".log")
    print_env_info(["torch", "torchvision", "numpy", "pandas"])
