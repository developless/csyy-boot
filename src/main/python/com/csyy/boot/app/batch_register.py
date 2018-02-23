#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.main.python.com.csyy.boot.app.common.utils.num_util import NumUtil
from src.main.python.com.csyy.boot.app.service.csapp_api import api
from src.main.resources.res import Resources

__author__ = 'Nice Wang'
__copyright__ = 'Copyright © maizijf.com All Rights Reserved'
__cake__ = '✨ 🍰 ✨'
'''
boot case application.
'''

resource = Resources('')
properties = resource.load()
env = properties['profile']['active']
print('env: %s' % env)
resource = Resources(env)
properties = resource.load()
host = properties['server']['host'] + properties['server']['context']
print('host: %s' % host)
#generator num
for x in range(2):
    user_info = NumUtil.gen_user_info()
    r = api(host, '')
    register_result = r.auto_register(user_info['mobile'])

    params = {
        "bankCardNo": user_info['bank_card'],
        "bankCode": user_info['bank_code'],
        "bankName": user_info['bank_name'],
        "bindType": "1",
        "idCardNo": user_info['id_card'],
        "mobile": user_info['mobile'],
        "userName": user_info['name'],
        "userId": register_result['nonoUserId']
    }
    a = api(host, register_result['sessionId'])
    a.open(params)



