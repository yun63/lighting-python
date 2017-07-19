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


def pick_by_weight(items):
    assert(isinstance(items, list))
    """
    根据权重概率随机（万分比)
    param: items [{..., "p": 2000}, {..., "p": 4000}]
    """
    total = sum([item.get('p', 0) for item in items])
    base = random.randint(0, int(total))
    curtotal = 0
    index = 0 
    for i, item in enumerate(items):
        print i, item
        curtotal = curtotal + item.get('p', 0)
        if base <= curtotal:
            index = i
            break
    picked_item = items[index]
    print 'base: %d, sum: %d, index: %d' % (base, total, index)
    return picked_item

def getNoDuplicateItems(items, n):
    assert(isinstance(items, list) and n <= len(items))
    result = []
    candidates = items[:]
    while n > 0:
        selected = pick_by_weight(candidates)
        candidates.remove(selected)
        result.append(selected)
        n -= 1
    return result


if __name__ == '__main__':
    items = [
        {'1': 100, 'p': 1000},
        {'2': 200, 'p': 2000},
        {'3': 300, 'p': 3000},
        {'4': 400, 'p': 4000},
        {'5': 500, 'p': 5000},
        {'6': 600, 'p': 6000}
    ]
    #item = pick_by_weight(items)
    #print item
    print getNoDuplicateItems(items, 2)
