import traceback

from functools import wraps

from flask import jsonify

from flora.libs.logger.logger import logger


def catch_func_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(repr(e))
            logger.error("%s error: %s" % (func.__name__, traceback.format_exc()))
    return wrapper


def catch_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(repr(e))
            logger.error("%s error: %s" % (func.__name__, traceback.format_exc()))
            return jsonify({'code': 5000, 'msg': '失败', 'data': ''})
    return wrapper
