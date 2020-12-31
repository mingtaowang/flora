# -*- coding: utf-8 -*-

from redis import Redis

from flora.config import REDIS_SERVER

redis = Redis(host=REDIS_SERVER.get('host'), port=REDIS_SERVER.get('port'),
              db=REDIS_SERVER.get('db', 0), password=REDIS_SERVER.get('password', None))
