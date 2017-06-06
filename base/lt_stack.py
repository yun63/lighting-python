# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: lt_stack.py

@Description: 栈

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心-斗地主项目组

@Create: 2017-06-06 15:14:53

"""

from base.lt_node import Node
from base.lt_exception import StackEmptyException


class Stack(object):
    def __init__(self):
        self._top = None
        self._size = 0

    @property
    def size(self):
        '''
        栈长度
        '''
        return self._size

    @property
    def top(self):
        '''
        取栈顶结点
        '''
        if self.empty():
            raise StackEmptyException()
        return self._top

    def empty(self):
        '''
        判空
        '''
        return self._size == 0

    def push(self, elem):
        '''
        入栈
        '''
        self._top = Node(elem, self._top)
        self._size += 1

    def pop(self):
        '''
        出栈
        '''
        if self.empty():
            raise StackEmptyException(-1, 'Empty Statck Exception')
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node

    def clear(self):
        '''
        清空栈
        '''
        while not self.empty():
            node = self.pop()
            del node

    def __iter__(self):
        current = self._top
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return ' '.join([item for item in self])

