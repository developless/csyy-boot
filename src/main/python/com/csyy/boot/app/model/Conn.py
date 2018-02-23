#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql as pymysql

__author__ = 'Nice Vip'
__copyright__ = 'Copyright © maizijf.com All Rights Reserved'
__cake__ = '✨ 🍰 ✨'
'''
security client application.
'''


class Conn(object):

    def __init__(self, host, port, user, password, db):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db


class MysqlConn(Conn):

    def __init__(self, host, port, user, password, db):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = 'utf8mb4'
        self.cursorclass = pymysql.cursors.DictCursor
