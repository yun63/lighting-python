# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: lt_stack_unittest.py

@Description:

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心-斗地主项目组

@Create: 2017-06-06 18:33:37

"""

import unittest

from base.lt_node import Node
from base.lt_stack import Stack
from base.lt_exception import StackEmptyException


class StackTestCase(unittest.TestCase):
    def setUp(self):
        self._stack = Stack()

    def test_size(self):
        self.assertEqual(self._stack.size, 0)

    def test_empty(self):
        self.assertEqual(self._stack.empty(), True)

    def test_pop(self):
        self._stack.push(123)

        try:
            node = self._stack.pop()
        except StackEmptyException as e:
            print (e.err_code, e.what)
        else:
            self.assertEqual(node.data, 123)

    def test_push(self):
        self._stack.push(123)
        self.assertEqual(self._stack.size, 1)
        self.assertEqual(self._stack.top.data, 123)

    def test_iterator(self):
        self._stack.push(1)
        self._stack.push(2)
        self._stack.push(3)
        self._stack.push(4)
        stlist = [i for i in self._stack]
        self.assertListEqual(stlist, [4, 3, 2, 1])

    def test_top(self):
        with self.assertRaises(StackEmptyException) as cm:
            top = self._stack.top
        e = cm.exception
        self.assertEqual(e.err_code, -1)
        self._stack.push(1)
        top = self._stack.top
        self.assertEqual(top.data, 1)
        self.assertEqual(self._stack.size, 1)

    def test_clear(self):
        self._stack.push(1)
        self._stack.clear()
        self.assertEqual(self._stack.size, 0)
        self.assertEqual(self._stack.empty(), True)
        self.assertEqual(self._stack._top, None)

    def tearDown(self):
        self._stack = None


if __name__ == '__main__':
    unittest.main()
