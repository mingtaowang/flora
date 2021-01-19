# -*- coding: utf-8 -*-

from redis import Redis
from flask_sqlalchemy import SQLAlchemy

from flora.config import REDIS_SERVER, SQLALCHEMY_DATABASE_URI

redis = Redis(host=REDIS_SERVER.get('host'), port=REDIS_SERVER.get('port'),
              db=REDIS_SERVER.get('db', 0), password=REDIS_SERVER.get('password', None))

mysql_db = SQLAlchemy()


def init_mysql(app=None):
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI.get('URI')
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI.get('URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_DATABASE_URI.get('TRACK_MODIFICATIONS')
    app.config["SQLALCHEMY_POOL_SIZE"] = SQLALCHEMY_DATABASE_URI.get('POOL_SIZE')
    app.config["SQLALCHEMY_ECHO"] = SQLALCHEMY_DATABASE_URI.get('ECHO')

    global mysql_db
    mysql_db.app = app
    mysql_db.init_app(app)
    mysql_db.create_all()
