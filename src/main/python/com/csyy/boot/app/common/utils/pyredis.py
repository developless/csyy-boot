#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Nice Wang'
__copyright__ = 'Copyright © maizijf.com All Rights Reserved'
__cake__ = '✨ 🍰 ✨'
'''
redis client application.
'''

import redis, operator


class PyRedis(object):
    def_config = {
        'host': '127.0.0.1',
        'port': 6379,
        'password': '',
        'db': 0
    }

    def __init__(self, **config):
        merged = dict(PyRedis.def_config)
        merged.update(config)
        self.config = merged
        self.pool = redis.ConnectionPool(**self.config)

    def jedis(self):
        return redis.Redis(connection_pool=self.pool)

    def execute(self, cmd):
        if cmd.strip() == '':
            return
        r = redis.Redis(connection_pool=self.pool)
        c, *a = cmd.split(' ')
        result = operator.methodcaller(c, *a)(r)
        print(result)
        return result


class PyRedisCmd(PyRedis):
    def cmd(self):
        s = input('>')
        while s != 'exit':
            self.execute(s)
            s = input('>')
