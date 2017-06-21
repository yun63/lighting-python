# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: str_util.py

@Description: 和字符串相关的处理接口

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-21 17:59:02

"""

import os
import uuid
import json
import base64


def uuid():
    """
    获取一个32位长的UUID字符串
    """
    return str(uuid.uuid4()).replace('-', '')

def get_env(key, default_val):
    """
    获取系统环境变量
    如果不存在，返回默认值
    """
    return os.environ.get(key, default_val)

def dumps(obj):
    """
    JSON的dumps方法，使用紧凑的数据格式
    如果在数据库中要保存json格式数据，会节省空间
    """
    return json.dumps(obj, separators=(',', ':'))

def base64_dumps(obj):
    """
    JSON的dumps方法，并对结果进行base64编码
    """
    jstr = json.dumps(obj, separators=(',', ':'))
    return base64.b64encode(jstr)

