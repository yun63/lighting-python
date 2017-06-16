# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: lt_list.py

@Description: 链表

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-16 15:14:36

"""


from base.lt_node import Node


class List(object):

    def __init__(self):
        self._head = Node()
