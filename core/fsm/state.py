# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: state.py

@Description: 状态类

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-26 16:59:18

"""


from core.entity import GameEntity


class State(GameEntity):
    """
    状态基类
    """
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def enter(self, entity):
        """ 实体进入本状态时执行
        """
        raise NotImplementedError

    def excute(self, entity):
        """ 实体状态更新方法
        """
        raise NotImplementedError

    def exit(self, entity):
        """ 实体退出本状态时执行
        """
        raise NotImplementedError

    def on_message(self, entity, telegram):
        """ 当实体收到消息时执行"""
        raise NotImplementedError

