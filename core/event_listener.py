# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: event_listener.py

@Description: 基于事件类的轻量级事件处理框架

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-15 18:40:03

"""

from util.event import EventBase

class EventDispatcher(object):

    def __init__(self):
        self._registry = {}

    def on(self, event_class, callback):
        self._register_event(event_class, callback)

    def off(self, event_class, callback):
        self._unregister_event(event_class, callback)

    def fire(self, event):
        assert(isinstance(event, EventBase))
        event_class = type(event)
        callbacks = self._registry.get(event_class)
        if callbacks:
            for cb in callbacks:
                try:
                    cb(event)
                except:
                    pass
        return None

    def _register_event(self, event_class, callback):
        cbs = self._registry.get(event_class)
        if cbs is None:
            self._registry[event_class] = [callback]
        else:
            self._registry[event_class] = list(set(cbs.append(callback)))

    def _unregister_event(self, event_class, callback):
        if callback is None:
            self._registry.pop(event_class, None)
        else:
            cbs = self._registry.get(event_class)
            try:
                cbs.remove(callback)
            except ValueError:
                pass

