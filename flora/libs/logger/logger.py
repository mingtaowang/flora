# -*-coding:utf-8-*-

import time
import os, sys
import logging


LOGGER_PATTERN = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def get_logger():
    direct_dir = get_save_path()
    print(direct_dir)
    handlers = [logging.FileHandler(direct_dir, encoding='utf-8')]
    kwargs = dict(handlers=handlers, format=LOGGER_PATTERN, level=logging.INFO)
    logging.basicConfig(**kwargs)
    logger = logging.getLogger(__name__)
    return logger


def get_save_path():
    if getattr(sys, "frozen", False):  # running in a bundle
        cur_dir = os.path.dirname(sys.executable)
    else:  # running as script
        cur_dir = os.getcwd()
    log_dir = os.path.join(cur_dir, 'log')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    dir = log_dir + '\\' + time.strftime("%Y-%m-%d", time.localtime()) + r'.log'
    return dir


logger = get_logger()

