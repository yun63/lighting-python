# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: serializer.py

@Description:

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-16 11:44:50

"""


class TYObject(object):
    """
    可视化对象
    定义了to_dict方法，可以把对象实例转换成字典，方便调试
    希望能够在调试信息中输出实例，那么那个实例的对象应该继承该类
    """
    def to_dict(self):
        return self._do_traverse_dict(self.__dict__)

    def __repr__(self):
        return u'|| %s == %s' % (self.__class__.__name__, self.to_dict())

    def __str__(self):
        return '|| %s == %s' % (self.__class__.__name__, self.to_dict())

    def _do_traverse_dict(self, inst_dict):
        out = {}
        for key, val in inst_dict.items():
            out[key] = self._do_traverse(key, val)
        return out

    def _do_traverse(self, key, val):
        if isinstance(val, TYObject):
            return val.to_dict()
        elif isinstance(val, dict):
            return self._do_traverse_dict(val)
        elif isinstance(val, list):
            return [self._do_traverse(key, i) for i in val]
        elif hasattr(val, '__dict__'):
            return self._do_traverse_dict(val.__dict__)
        else:
            return val
        return None

