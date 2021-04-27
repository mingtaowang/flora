# -*-coding:utf-8-*-

import os, sys

from configparser import ConfigParser


def get_current_dir():
    if getattr(sys, "frozen", False):  # running in a bundle
        cur_dir = os.path.dirname(sys.executable)
    else:  # running as script
        cur_dir = os.path.dirname(os.path.abspath(__file__))
    return cur_dir


class Config(object):
    def __init__(self):
        cf = ConfigParser()
        base_dir = get_current_dir()
        conf_file = os.path.join(base_dir, "config.conf")
        cf.read(conf_file)

        self.http_host = cf.get("start", "HTTP_HOST")
        self.http_port = cf.getint("start", "HTTP_PORT")
        self.debug = cf.get("start", "DEBUG")

        self.base_path = cf.get("suspect", "BASE_PATH")
        self.run_time = cf.get("task", "RUN_TIME")


CONFIG = Config()
