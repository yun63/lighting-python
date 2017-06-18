#-*- coding:utf-8 -*-

###############################################################################
#
# Copyright © 2017 LT. All Rights Reserved.
#
###############################################################################

"""
@File: time_util.py

@Brief: 与时间相关的函数

@Author: leiyunfei

@Email: leiyunfei@tuyoogame.com

@Create: 2017-06-18 22:22:41

"""


import time
from datetime import datetime
from __future__ import unicode_literals, absolute_import

def current_timestamp():
    return int(time.time());

def strdateftime(date_str, format='%Y-%m-%d %H:%M:%S'):
    """
    把日期字符串转换成datetime日期格式
    """
    return datetime.strftime(date_str, format)

def strftime(date_str, format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(date_str, format)

def timestr(dt, format='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(format)

def seconds_diff(start, end):
    """
    获取两个字符串时间的时间差，单位是秒数
    时间字符串格式:%Y-%m-%d %H:%M:%S.%f
    """
    format = '%Y-%m-%d %H:%M:%S.%f'
    t1 = datetime.strftime(start, format)
    t2 = datetime.strftime(end, format)
    diff = t2 - t1
    return diff.days * 86400 + diff.secs

def from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)

def to_timestamp(dt):
    return int(time.mktime(dt))

def strf_timestamp(date_str):
    return int(time.mktime(time.strftime(date_str, '%Y-%m-%d %H:%M:%S')))

