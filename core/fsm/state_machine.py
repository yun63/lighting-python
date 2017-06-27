# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: state_machine.py

@Description: 有限状态机

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-23 18:11:04

"""

from core.serializer import TYObject
from core.fsm.state import State


class StateMachine(TYObject):
    """
    有限状态自动机
    """
    def __init__(self, entity):
        # 该状态机所属实体
        self._owner = entity
        # 当前状态
        self._current_state = None
        # 前一个状态
        self._previous_state = None
        # 全局状态，状态机每次更新时都要调用全局状态的excute方法
        self._global_state = None
        # 状态机拥有的状态集合{key=name, value=State()}
        self._state_entries = {}

    @property
    def current_state(self):
        """ 获取当前状态
        """
        return self._current_state

    @property
    def global_state(self):
        """ 获取全局状态
        """
        return self._global_state

    @property
    def previous_state(self):
        """ 获取当前状态的前一个状态
        """
        return self._previous_state

    def set_global_state(self, state_name):
        """ 设置全局状态
        """
        self._global_state = self._state_entries.get(state_name)

    def set_current_state(self, state_name):
        """ 设置当前状态
        """
        self._current_state = self._state_entries.get(state_name)


    def set_previous_state(self, state_name):
        """ 设置前一个状态
        """
        self._previous_state = self._state_entries.get(state_name)

    def update(self):
        """ 更新状态机的方法
        """
        if self._global_state:
            # 执行全局状态的方法
            self._global_state.excute(self._owner)

        if self._current_state:
            # 执行当前状态的方法
            self._current_state.excute(self._owner)

    def register_state(self, state):
        """ 注册子状态
        """
        self._state_entries[state.name] = state

    def get_state_by_name(self, name):
        """ 通过名称获取状态实例
        """
        return self._state_entries.get(name)

    def handle_message(self, msg):
        """ 处理消息
        """
        # 首先检查当前状态是否可以处理消息
        if self._current_state and \
           self._current_state.on_message(self._owner, msg):
            return True
        # 当前状态不能处理消息，那么再检查全局状态能否处理消息
        if self._global_state and \
           self._global_state.on_message(self._owner, msg):
            return True
        return False

    def isinstate(self, name):
        """ 判断是否状态机正处于指定的状态中
        """
        return self._current_state.name == name

    def change_state(self, new_state):
        """ 状态机更新状态
        """
        assert(isinstance(new_state, State))

        # 保存前一个状态的记录
        self._previous_state = self._current_state;
        # 执行当前状态的退出方法
        self._current_state.exit(self._owner)
        # 新状态改变为当前的状态
        self._current_state = new_state
        # 执行新状态的enter方法
        self._current_state.enter(self._owner)

    def revert_previous(self):
        """ 回退到上一个状态
        """
        self.change_state(self._previous_state)

