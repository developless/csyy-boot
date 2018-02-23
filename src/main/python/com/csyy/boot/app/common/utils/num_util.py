#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from datetime import date, timedelta

import re

from src.main.python.com.csyy.boot.app.common.consts.consts import Consts

__author__ = 'Nice Wang'
__copyright__ = 'Copyright © maizijf.com All Rights Reserved'
__cake__ = '✨ 🍰 ✨'
'''
number client application.
'''


class NumUtil(object):
    mobile_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "170", "186", "187", "188", "189"]
    id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]

    @classmethod
    def gen_mobile(cls):
        return random.choice(NumUtil.mobile_list) + "".join(random.choice("0123456789") for i in range(8))

    @classmethod
    def validate_id_card(cls, id_card):
        if len(id_card) != 18:
            return False, "Length error"
        if not re.match(r"^\d{17}(\d|X|x)$", id_card):
            return False, "Format error"
        if id_card[0:6] not in Consts.area_dict:
            return False, "Area code error"
        try:
            date(int(id_card[6:10]), int(id_card[10:12]), int(id_card[12:14]))
        except ValueError as ve:
            return False, "Datetime error: {0}".format(ve)
        if str(NumUtil.check_code_list[
                   sum([a * b for a, b in zip(NumUtil.id_code_list, [int(a) for a in id_card[0:-1]])]) % 11]) != \
                str(id_card.upper()[-1]):
            return False, "Check code error"
        return True, "{}省 {}市 {}".format(Consts.area_dict[id_card[0:2] + "0000"].rstrip("省"),
                                         Consts.area_dict[id_card[0:4] + "00"].rstrip("市"),
                                         Consts.area_dict[id_card[0:6]])

    @classmethod
    def gen_id_card(cls, area_code, age, gender):
        if str(area_code) not in Consts.area_dict.keys():
            return None
        birth = str(date(date.today().year - age, 1, 1) + timedelta(days=random.randint(0, 364))).replace("-", "")
        rd = random.randint(0, 999)
        if gender == 0:
            gender_num = rd if rd % 2 == 0 else rd + 1
        else:
            gender_num = rd if rd % 2 == 1 else rd - 1
        result = str(area_code) + birth + str(gender_num).zfill(3)
        return result + str(
            NumUtil.check_code_list[sum([a * b for a, b in zip(NumUtil.id_code_list, [int(a) for a in result])]) % 11])

    @classmethod
    def gen_name(cls):
        first_name = random.choice([x for x in Consts.first_names])
        mid_name = random.choice([x for x in Consts.last_names])
        last_name = random.choice([x for x in Consts.last_names])
        name = first_name + mid_name + last_name
        return name

    @classmethod
    def gen_bank_no(cls):
        return "622522"+"".join(random.choice("0123456789") for i in range(10))

    @classmethod
    def gen_user_info(cls):
        first_name = random.choice([x for x in Consts.first_names])
        mid_name = random.choice([x for x in Consts.last_names])
        last_name = random.choice([x for x in Consts.last_names])
        name = first_name + mid_name + last_name
        age = random.choice([x for x in range(18, 99)])
        gender = random.choice([0, 1])
        area_code = random.choice([x for x in Consts.area_dict.keys()])
        id_card = NumUtil.gen_id_card(int(area_code), age, gender)

        return {
            'name': name,
            'age': age,
            'gender': gender,
            'id_card': id_card,
            'area_code': area_code,
            'bank_card': NumUtil.gen_bank_no(),
            'bank_code': 'SPDB',
            'bank_name': '浦发银行',
            'mobile': NumUtil.gen_mobile()
            }
