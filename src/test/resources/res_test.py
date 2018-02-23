#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.main.resources.res import Resources

__author__ = 'Nice Wang'
__copyright__ = 'Copyright © maizijf.com All Rights Reserved'
__cake__ = '✨ 🍰 ✨'
'''
boot case application.
'''

env = 'stb'
r = Resources(env)
load = r.load()
# 遍历迭代器
for data in load:
    print(type(data))
    print(data)
    print("---" * 25)