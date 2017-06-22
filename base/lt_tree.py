#-*- coding:utf-8 -*-

###############################################################################
#
# Copyright © 2017 LT. All Rights Reserved.
#
###############################################################################

"""
@File: btree.py

@Brief: 二叉树

@Author: leiyunfei

@Email: leiyunfei@tuyoogame.com

@Create: 2017-05-24 23:43:39

"""


class BintreeNode(object):
    def __init__(self, lnode=None, rnode=None, data=None):
        self.left = lnode
        self.right = rnode
        self.data = data
        

class BinaryTree(object):
    def __init__(self, data, visitor):
        self._root = BintreeNode(data=data)
        self._visitor = visitor

    @property
    def root(self):
        return self._root

    def insert(self, data):
        if data < self.root.data:
            self._insert_left_sub_tree(data, self.root)
        else:
            self._insert_right_sub_tree(data, self.root)

    def _insert_left_sub_tree(self, data, node):
        if node.left is not None:
            self._insert_left_sub_tree(self, data, node.left)
        else:
            node.left = BintreeNode(data=data)

    def _insert_right_sub_tree(self, data, node):
        if node.right is not None:
            self._insert_right_sub_tree(data, node.right)
        else:
            node.right = BintreeNode(data=data)
