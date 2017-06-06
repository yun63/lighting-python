#-*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: random_util.py

@Description:

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心-斗地主项目组

@Create: 2017-05-22 10:57:55

"""


import random
import json


def pick_by_weight(items):
    assert(isinstance(items, list))
    """
    根据权重概率随机（万分比)
    param: items [{"item": {}, "p": 2000}, {"item": {}, "p": 4000}]
    """
    total = sum([item.get('p', 0) for item in items])
    print total
    base = random.randint(0, int(total))
    curtotal = 0
    index = None
    for i, item in enumerate(items):
        print i, item
        curtotal = curtotal + item.get('p', 0)
        if base <= curtotal:
            index = i
            break
    pickedItem = items[index]
    print 'base: %d, sum: %d, index: %d' % (base, total, index)
    return pickedItem.get('item', {})


if __name__ == '__main__':
    items = [
        {'item': {'lei': 100, 'yun': 200, 'fei': 300}, 'p': 100},
        {'item': {'lei': 1000, 'yun': 2000, 'fei': 3000}, 'p': 9000},
        {'item': {'lei': 10000, 'yun': 20000, 'fei': 30000}, 'p': 200}
    ]
    item = pick_by_weight(items)
    print item
