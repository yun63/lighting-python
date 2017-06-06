# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: lt_node.py

@Description: 基础数据结构结点类型定义

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心-斗地主项目组

@Create: 2017-06-05 16:01:19

"""

class LinkNode(object):
    def __init__(self, elem, node=None):
        self.elem = elem
        self.next = node

