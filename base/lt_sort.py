# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: lt_sort.py

@Description:

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-08-28 14:52:43

"""


def bubble_sort(seq, compred):
    """
    冒泡排序算法
    @param: seq 待排序列表
    @param: compred 二元比较函数
    @return: 排好序的列表
    """
    n = len(seq)
    for i in range(n):
        for j in range(1, n - i):
            if compred(seq[j], seq[j-1]):
                seq[j-1], seq[j] = seq[j], seq[j-1]
    return seq

