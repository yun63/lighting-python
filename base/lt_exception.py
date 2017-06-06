# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: lt_exception.py

@Description: 异常

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心-斗地主项目组

@Create: 2017-06-05 16:16:56

"""

import sys

class LTException(Exception):
    def __init__(self, err_code, message):
        super(LTException, self).__init__(err_code, message)

    @property
    def err_code(self):
        return self.args[0]

    @property
    def what(self):
        return self.args[1]

    def __str__(self):
        return '%s: %s' % (self.err_code, self.what)

    def __unicode__(self):
        return u'%s: %s' % (self.err_code, self.what)


class QueueEmptyException(LTException):
    def __init__(self,  **argd):
        super(QueueEmptyException, self).__init__(-1, 'Empty Queue Exception')
        caller_cls_name = ''
        try:
            caller = argd.get('caller', None)
            if caller:
                if not hasattr(caller, '__name__'):
                    caller_cls_name = caller.__class__
                caller_cls_name = caller.__name__
        except:
            pass
        self._oper = '[ ' + caller_cls_name + '.' + sys._getframe().f_back.f_back.f_code.co_name + ' ]'

    def __str__(self):
        return '%s: %s occured %s' % (self.err_code, self.what, self._oper)

