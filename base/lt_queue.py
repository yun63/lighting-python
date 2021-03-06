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

import heapq

from base.lt_exception import QueueEmptyException
from base.lt_node import Node

class Queue(object):

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def size(self):
        '''
        队列长度
        '''
        return self._size

    @property
    def front(self):
        '''
        取队头结点
        如果队列为空，抛出异常
        '''
        if self.empty():
            raise QueueEmptyException()
        return self._front

    @property
    def rear(self):
        '''
        取队尾结点
        如果队列为空，抛出异常
        '''
        if self.empty():
            raise QueueEmptyException()
        return self._rear

    def empty(self):
        '''
        判空
        '''
        return self._size == 0

    def enque(self, item):
        '''
        入队列
        '''
        rear = self._rear
        self._rear = Node(item)
        if self.empty():
            self._front = self._rear
        else:
            rear.next = self._rear
        self._size += 1

    def deque(self):
        '''
        出队列
        如果队列为空，抛出异常
        '''
        if self.empty():
            raise QueueEmptyException()
        node = self._front
        self._front = self._front.next
        self._size -= 1
        return node

    def clear(self):
        '''
        清空队列
        '''
        for item in self:
            del item
        self._front = self._rear = None
        self._size = 0

    def __iter__(self):
        '''
        迭代，遍历队列
        '''
        current = self._front
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return ' '.join([str(item) for item in self])

    def __repr__(self):
        return 'Queue(' + str(self) + ')'


class PriorityQueue(object):
    '''
    优先级队列
    '''
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

