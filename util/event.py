# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: event.py

@Description:

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-15 21:13:58

"""

import time

class EventBase(object):

    def __init__(self):
        self.timestamp = int(time.time())

    def __repr__(self):
        return self.__class__.__name__
