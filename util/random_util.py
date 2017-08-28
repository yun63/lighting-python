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


def pick_by_p(items):
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
        curtotal = curtotal + item.get('p', 0)
        if base <= curtotal:
            index = i
            break
    picked_item = items[index]
    #print 'base: %d, sum: %d, index: %d' % (base, total, index)
    return picked_item

def getNoDuplicateItems(items, n):
    assert(isinstance(items, list) and n <= len(items))
    result = []
    candidates = items[:]
    while n > 0:
        selected = pick_by_p(candidates)
        candidates.remove(selected)
        result.append(selected.get('id'))
        n -= 1
    return result


if __name__ == '__main__':
    
    fruits = [
        {
            "id": 1,
            "kind": 1,
            "name": "苹果",
            "times": 2,
            "p": 200,
            "eventid": 0
        },
        {
            "id": 2,
            "kind": 2,
            "name": "橘子",
            "times": 2,
            "p": 300,
            "eventid": 0
        },
        {
            "id": 3,
            "kind": 3,
            "name": "柠檬",
            "times": 2,
            "p": 400,
            "eventid": 0
        },
        {
            "id": 4,
            "kind": 4,
            "name": "草莓",
            "times": 2,
            "p": 300,
            "eventid": 0
        },
        {
            "id": 5,
            "kind": 5,
            "name": "葡萄",
            "times": 2,
            "p": 200,
            "eventid": 0
        },
        {
            "id": 6,
            "kind": 6,
            "name": "樱桃",
            "times": 2,
            "p": 100,
            "eventid": 0
        },
        {
            "id": 7,
            "kind": 7,
            "name": "西瓜",
            "times": 2,
            "p": 100,
            "eventid": 0
        },
        {
            "id": 8,
            "kind": 8,
            "name": "Num7",
            "times": 2,
            "p": 100,
            "eventid": 0
        },
        {
            "id": 9,
            "kind": 1,
            "name": "苹果",
            "times": 5,
            "p": 100,
            "eventid": 1
        },
        {
            "id": 10,
            "kind": 2,
            "name": "橘子",
            "times": 10,
            "p": 100,
            "eventid": 2
        },
        {
            "id": 11,
            "kind": 3,
            "name": "柠檬",
            "times": 15,
            "p": 100,
            "eventid": 2
        },
        {
            "id": 12,
            "kind": 4,
            "name": "草莓",
            "times": 20,
            "p": 100,
            "eventid": 3
        },
        {
            "id": 13,
            "kind": 5,
            "name": "葡萄",
            "times": 30,
            "p": 100,
            "eventid": 3
        },
        {
            "id": 14,
            "kind": 6,
            "name": "樱桃",
            "times": 50,
            "p": 100,
            "eventid": 3
        },
        {
            "id": 15,
            "kind": 7,
            "name": "西瓜",
            "times": 100,
            "p": 100,
            "eventid": 3
        },
        {
            "id": 16,
            "kind": 8,
            "name": "Num7",
            "times": 200,
            "p": 100,
            "eventid": 3
        }
    ]

    ret = []
    for i in xrange(100000):
        tt = getNoDuplicateItems(fruits, 2)
        if tt[0] == tt[1]:
            print('duplicate id %d' % tt[0])
        ret.append(tt)
    #print ret
