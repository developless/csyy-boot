#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from src.main.python.com.csyy.boot.app.common.utils.pyredis import PyRedis
from src.main.python.com.csyy.boot.app.common.utils.pysql import PySql

__author__ = 'Nice Wang'
__copyright__ = 'Copyright © maizijf.com All Rights Reserved'
__cake__ = '✨ 🍰 ✨'
'''
gensession case application.
'''
import uuid


class SessionCtx(object):

    def __init__(self, **properties):
        mysql_config = properties['mysql']
        codis_config = properties['codis']
        self.sql_template = PySql(**mysql_config)
        self.redis_template = PyRedis(**codis_config)

    def user_info(self, **kv):
        user_codes = ','.join(kv.keys())
        sql_format = 'select u.user_code, u.mobile_number, d.real_name, d.certificate_number from user u, user_detail d where u.user_code = d.user_code and u.user_code in ('
        sql = sql_format + user_codes + ')'
        result = self.sql_template.execute(sql)
        sessionIds = []
        for entity in result:
            user_code = entity['user_code']
            user_id = int(kv[str(user_code)])
            session = {
                'userCode':user_code,
                'nonoUserId':user_id,
                'sessionMobileNumber':entity['mobile_number'],
                'sessionUserName':entity['real_name'],
                'userInfo':{
                    'idcardNo':entity['certificate_number'],
                    'realName':entity['real_name'],
                    'userName':entity['real_name'],
                    'userCode':user_code,
                    'mobileNumber':entity['mobile_number'],
                    'nonoUserId':user_id
                }
            }  
            sessionId = str(uuid.uuid1()).replace('-', '')
            sessionIds.append(sessionId)
            print('session:' + sessionId)
            self.redis_template.jedis().set('session:' + sessionId, json.dumps(session), 3600 * 24 * 3)
        return sessionIds