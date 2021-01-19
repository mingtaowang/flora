# -*- coding: utf-8 -*-

from flora.libs.db.store import mysql_db


def insert_one(name, password):
    sql = "insert into users (name, password) values ('%s', '%s')" % (name, password)
    mysql_db.session.execute(sql)
    mysql_db.session.commit()
