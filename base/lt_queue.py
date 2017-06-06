# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: lt_queue.py

@Description: 队列实现

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心-斗地主项目组

@Create: 2017-06-05 16:00:34

"""

from base.lt_exception import QueueEmptyException

class Node(object):
    def __init__(self, elem):
        self.data = elem
        self.next = None


class Queue(object):
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    @property
    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def enque(self, item):
        rear = self._rear
        self._rear = Node(item)
        if self.empty():
            self._front = self._rear
        else:
            rear.next = self._rear
        self._size += 1

    def deque(self):
        if self.empty():
            raise QueueEmptyException(caller=self)
        node = self._front
        self._front = self._front.next
        self._size -= 1
        return node.data


    def front(self):
        if self.empty():
            raise QueueEmptyException(caller=self)
        return self._front.data

    def rear(self):
        if self.empty():
            raise QueueEmptyException(caller=self)
        return self._rear.data

    def __iter__(self):
        current = self._front
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return ' '.join([str(item) for item in self])

    def __repr__(self):
        return 'Queue(' + str(self) + ')'

