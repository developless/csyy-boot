#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uuid

__author__ = 'Nice Wang'
__copyright__ = 'Copyright © maizijf.com All Rights Reserved'
__cake__ = '✨ 🍰 ✨'
'''
security client application.
'''
import requests, json


class api(object):

    def __init__(self, host, sessionId):
        self.host = host
        self.sessionId = sessionId
        self.headers = {
            'content-type': 'application/json',
            'sessionId': sessionId,
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        }
        self.no_auth_headers = {
            'content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        }

    def recharge(self, params):
        apply_url = '/v5/account/rechargeApply?amount=' + params
        print(self.host + apply_url)
        apply_result = requests.get(self.host + apply_url, headers=self.headers)
        print(apply_result.text)
        json_result = json.loads(apply_result.text)
        confirm_param = json_result['data'] 
        confirm_param['smsCode'] = '123456'
        confirm_url = '/v5/account/rechargeConfirm'
        print(self.host + confirm_url)
        result = requests.post(self.host + confirm_url, data=json.dumps(confirm_param), headers=self.headers)
        print (result.text)
        return result   

    def invest(self, params):
        url = '/v5/invest/commit?sessionId=' + self.sessionId
        print(self.host + url)
        result = requests.post(self.host + url, data=json.dumps(params), headers=self.headers)
        print (result.text)
        return result

    def register(self, params):
        url = '/v5/register/doRegister'
        print(self.host + url)
        result = requests.post(self.host + url, data=json.dumps(params), headers=self.no_auth_headers)
        print (result.text)
        return result

    def auto_register(self, mobile):
        url = '/v5/register/doRegister?client_type=iOS&deviceNo='+str(uuid.uuid1()).replace('-', '')
        print(self.host + url)

        params = {
            "blackBox": str(uuid.uuid1()).replace('-', ''),
            "checkCode": "888888",
            "mobileNumber": mobile,
            "password": "a123456",
            "registerApproach": "04",
            "resource": "CSYY"
        }
        result = requests.post(self.host + url, data=json.dumps(params), headers=self.no_auth_headers)
        print (result.text)
        json_result = json.loads(result.text)
        return json_result['data']

    def open (self, params):
        url = '/v5/bankCard/bindApply'
        print(self.host + url)
        apply_result = requests.post(self.host + url, data=json.dumps(params), headers=self.headers)
        print(apply_result.text)
        json_result = json.loads(apply_result.text)
        confirm_param = json_result['data']
        confirm_param['smsCode'] = '123456'
        confirm_param['userId'] = params['userId']
        confirm_url = '/v5/bankCard/bindConfirm'
        print(self.host + confirm_url)
        result = requests.post(self.host + confirm_url, data=json.dumps(confirm_param), headers=self.headers)
        print (result.text)
        return result
