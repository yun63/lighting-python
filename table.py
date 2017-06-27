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

import time

from core.event import EventBase
from core.event_listener import EventDispatcher
from core.fsm.state import State
from core.fsm.state_machine import StateMachine


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

class TableStateIdle(State):

    def __init__(self):
        super(TableStateIdle, self).__init__('idle')

    def enter(self, table):
        print '%s enter %s state' % (table, self.name)

    def excute(self, table):
        print '%s excute %s state, ZZZZZZ...' % (table, self.name)
        time.sleep(5)
        table.fsm.change_state(table.fsm.get_state_by_name('calling'))

    def exit(self, table):
        print '%s exit %s state, byebye!!!' % (table, self.name)


class TableStateCalling(State):

    def __init__(self):
        super(TableStateCalling, self).__init__('calling')

    def enter(self, table):
        print '%s enter %s state!' % (table, self.name)

    def excute(self, table):
        table._callings += 1
        print '%s excute %s state!' % (table, self.name)
        time.sleep(2)
        new_state = table.fsm.get_state_by_name('playing')
        table.fsm.change_state(new_state)

    def exit(self, table):
        print '%s exit %s state!' % (table, self)
        table._callings -= 1

class TableStatePlaying(State):

    def __init__(self):
        super(TableStatePlaying, self).__init__('playing')

    def enter(self, table):
        print '%s enter %s state!' % (table, self.name)

    def excute(self, table):
        print '%s excute %s state, playing, playing' % (table, self)
        time.sleep(5)
        idle_state = table.fsm.get_state_by_name('idle')
        table.fsm.change_state(idle_state)

    def exit(self, table):
        print '%s exit %s state!' % (table, self)

class Table(EventDispatcher):
    
    def __init__(self, table_id):
        super(Table, self).__init__()
        self._table_id = table_id
        self._seats = []
        self._callings = 0
        self._setup_events()
        self._fsm = None
        # 建立状态机
        self._setup_fsm()

    def _setup_fsm(self):
        print 'setup fsm'
        self._fsm = StateMachine(self)
        self._fsm.register_state(TableStateIdle())
        self._fsm.register_state(TableStateCalling())
        self._fsm.register_state(TableStatePlaying())
        self._fsm.set_current_state('idle')
        print len(self._fsm._state_entries)
        for st in self._fsm._state_entries:
            print st

    @property
    def table_id(self):
        return self._table_id

    @property
    def fsm(self):
        """ 返回桌子的状态机
        """
        return self._fsm

    def sitdown(self, user_id, seat_id):
        self.seats.append(seat_id)
        self.fire(SitdownEvent(user_id, self.table_id, seat_id))

    @property
    def seats(self):
        return self._seats

    def update(self):
        self._fsm.update()

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


import pdb
from core.entity import GameEntity

if __name__ == '__main__':
    table = Table(1);
    while True:
        table.update()

