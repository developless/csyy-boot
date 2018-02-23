#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.main.python.com.csyy.boot.app.service.csapp_api import api
from src.main.python.com.csyy.boot.app.service.gensession import SessionCtx
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

ctx = SessionCtx(**properties)
#args {'user_code':'user_id'}
args = {'1001967253':'7700246'}
sessions = ctx.user_info(**args)

for sessionId in sessions:
    #new a api object
    a = api(host, sessionId)
    #recharge(amount)
    a.recharge('10000')
    #invest(productId, amount)
    a.invest({'productId':'8438', 'amount':'1000'})

