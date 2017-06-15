# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: table.py

@Description:

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-15 21:23:31

"""


from util.event import EventBase
from util.event_listener import EventDispatcher


class Table(EventDispatcher):
    
    def __init__(self, table_id):
        super(Table, self).__init__()
        self._table_id = table_id
        self._seats = []
        self._setup_events()

    @property
    def table_id(self):
        return self._table_id

    @property
    def seats(self):
        return self._seats

    def _setup_events(self):
        self.on(EventBase, self._handle_event)

    def _handle_event(self, event):
        print event


if __name__ == '__main__':
    table = Table(1);
    print table._registry
    table.fire(EventBase())
