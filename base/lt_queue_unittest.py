# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: lt_queue_unittest.py

@Description: 队列单元测试

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心-斗地主项目组

@Create: 2017-06-06 11:03:41

"""

import unittest

from base.lt_node import Node
from base.lt_queue import Queue
from base.lt_exception import QueueEmptyException


class QueueTestCase(unittest.TestCase):
    def setUp(self):
        self._queue = Queue()

    def test_empty(self):
        self.assertEqual(self._queue.empty(), True)

    def test_size(self):
        self.assertEqual(self._queue.size, 0)

    def test_enque(self):
        self._queue.enque({'a': 1})
        self.assertEqual(self._queue.empty(), False)
        self.assertEqual(self._queue.size, 1)
        self.assertEqual(self._queue.front, self._queue.rear)

    def test_deque(self):
        with self.assertRaises(QueueEmptyException) as cm:
            self._queue.deque()
        e = cm.exception
        self.assertEqual(e.err_code, -1)
        self._queue.enque(123)
        try:
            node = self._queue.deque()
        except QueueEmptyException as e:
            pass
        else:
            self.assertEqual(node.data, 123)

    def test_front(self):
        try:
            self._queue.enque(1)
            self._queue.enque({'a': 2})
            self._queue.enque(100)
            self._queue.enque('leiyunfei')
            node = self._queue.front
        except QueueEmptyException as e:
            print (e.err_code, e.what)
        else:
            self.assertEqual(node.data, 1)

    def test_rear(self):
        self._queue.enque(1)
        self._queue.enque({'a': 2})
        self._queue.enque(100)
        self._queue.enque('leiyunfei')
        try:
            node = self._queue.rear
        except QueueEmptyException as e:
            print (e.err_code, e.what)
        else:
            self.assertEqual(node.data, 'leiyunfei')

    def test_iterator(self):
        self._queue.enque(1)
        self._queue.enque({'a': 2})
        self._queue.enque(100)
        self._queue.enque('leiyunfei')
        q = [elem for elem in self._queue]
        self.assertListEqual(q, [1, {'a': 2}, 100, 'leiyunfei'])

    def tearDown(self):
        self._queue = None


if __name__ == '__main__':
    unittest.main()
        
