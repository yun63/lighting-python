# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: lt_search.py

@Description: 查找算法

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-08-28 15:04:56

"""


def bsearch(seq, key):
    """
    二分查找算法
    @param: seq 目标序列
    @param: key 关键字
    @return: 关键字索引: 查找成功 None: 查找失败，没有关键字
    """
    low = 0
    hight = len(seq) - 1
    while low <= hight:
        mid = low + (hight - low) // 2
        if seq[mid] < key
            low  = mid + 1
        elif seq[mid] > key:
            hight = mid - 1
        else:
            return mid
    return None

def _compute_next(patten):
    n = len(patten)
    next_prefix = [0] * n
    j = 0


def kmp(string, patten):
    """
    KMP模式匹配算法
    @param: string 母串
    @param: patten 模式串
    @return: patten在string中对应的位置序列
    """
    m = len(patten)
    n = len(string)
    offsets = []

    if m > n:
        return offsets

    nextarr = _compute_next(patten)




