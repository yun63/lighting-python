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

def current_timestr():
    ct = datetime.now()
    return ct.strftime('%Y-%m-%d %H:%M:%S')

def from_timestr(date_str, format='%Y-%m-%d %H:%M:%S'):
    """
    返回字符串日期格式的datetime表示
    '2017-06-19 15:13:50' -> datetime.datetime(2017, 6, 19, 15, 13, 50)
    """
    return datetime.strptime(date_str, format)

def to_timestr(dt, format='%Y-%m-%d %H:%M:%S'):
    """
    返回指定日期的字符串表示
    datetime.datetime(2017, 6, 19, 15, 13, 50) -> '2017-06-19 15:13:50'
    """
    return dt.strftime(format)

def seconds_diff(start, end):
    """
    获取两个日期之间的时间差，单位是秒数
    时间字符串格式:%Y-%m-%d %H:%M:%S.%f
    """
    format = '%Y-%m-%d %H:%M:%S'
    t1 = datetime.strftime(start, format)
    t2 = datetime.strftime(end, format)
    diff = t2 - t1
    return diff.days * 86400 + diff.secs

def from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)

def datetime_to_timestamp(dt):
    return int(time.mktime(dt.timetuple()))

def strtime_to_timestamp(date_str):
    return int(time.mktime(time.strptime(date_str, '%Y-%m-%d %H:%M:%S')))

def lapsed_seconds():
    """
    获取今日零点到现在已过去的时间秒数
    """
    timestamp = int(time.time())
    nt = time.localtime(timestamp)
    return nt[3] * 3600 + nt[4] * 60 + nt[5]

def left_seconds():
    """
    获取今日剩余的时间秒数
    """
    return 86400 - lapsed_seconds()

def is_same_day(timestamp1, timestamp2):
    return datetime.fromtimestamp(timestamp1).date() == datetime.fromtimestamp(timestamp2).date()

