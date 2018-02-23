#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Nice Wang'
__copyright__ = 'Copyright © maizijf.com All Rights Reserved'
'''
redis client application.
'''

import yaml
import codecs
import os


class Resources(object):
    resource_prefix = os.path.dirname(os.path.abspath(__file__)) + '/application'
    resource_append = '.yml'

    def __init__(self, profile):
        self.profile = profile
        if profile == '':
            self.resource_name = Resources.resource_prefix + Resources.resource_append
        else:
            self.resource_name = Resources.resource_prefix + '-' + profile + Resources.resource_append

    def load(self):
        fp = codecs.open(self.resource_name, "r", "utf-8")
        document = fp.read()
        fp.close()
        # 将yaml格式内容 转换成 dict类型
        return yaml.load(document)

