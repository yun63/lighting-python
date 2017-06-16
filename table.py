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


from core.event import EventBase
from core.event_listener import EventDispatcher


class SitdownEvent(EventBase):

    def __init__(self, user_id, table_id, seat_id):
        super(SitdownEvent, self).__init__()
        self.user_id = user_id
        self.table_id = table_id
        self.seat_id = seat_id


class SitdownEvent(EventBase):

    def __init__(self, user_id, table_id, seat_id):
        super(SitdownEvent, self).__init__()
        self.table_id = table_id
        self.user_id = user_id
        self.seat_id = seat_id

class Table(EventDispatcher):
    
    def __init__(self, table_id):
        super(Table, self).__init__()
        self._table_id = table_id
        self._seats = []
        self._setup_events()

    @property
    def table_id(self):
        return self._table_id

    def sitdown(self, user_id, seat_id):
        self.seats.append(seat_id)
        self.fire(SitdownEvent(user_id, self.table_id, seat_id))

    @property
    def seats(self):
        return self._seats

    def sitdown(self, user_id, seat_id):
        self.fire(SitdownEvent(user_id, self.table_id, seat_id))

    def _setup_events(self):
        self.on(EventBase, self._handle_event)
        self.on(SitdownEvent, self._handle_sitdown_event)

    def _handle_event(self, event):
        print event

    def _handle_sitdown_event(self, event):
        if isinstance(event, SitdownEvent):
            print event
<<<<<<< HEAD
            print event.seat_id, event.seat_id, event.timestamp
=======
>>>>>>> 5979878d8c8648895c4611f19cb367cd346a0d6b


if __name__ == '__main__':
    table = Table(1);
<<<<<<< HEAD
    #table.fire(EventBase())
    table.sitdown(110001, 10001)

=======
    print table._registry
    table.fire(EventBase())
    table.sitdown(10001, 4)
>>>>>>> 5979878d8c8648895c4611f19cb367cd346a0d6b
