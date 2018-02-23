#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Nice Wang'
__copyright__ = 'Copyright © maizijf.com All Rights Reserved'
__cake__ = '✨ 🍰 ✨'
'''
mysql client application.
'''

import pymysql


class PySql(object):
    def_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'boot',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }

    def __init__(self, **config):
        merged = dict(PySql.def_config)
        merged.update(config)
        self.config = merged

    def execute(self, sql):
        if sql.strip() == "":
            return
        print(self.config)
        connection = pymysql.connect(**self.config)
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                connection.commit()
                print(result)
                return result
        except Exception:
            connection.rollback()
        finally:
            connection.close()


class CmdPySql(PySql):

    def cmd(self):
        s = input('>')
        while s != 'exit':
            for sql in s.split(';'):
                self.execute(sql)
            s = input('>')
