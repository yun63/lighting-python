# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: entity.py

@Description:

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-26 15:28:12

"""


from core.serializer import TYObject


class GameEntity(TYObject):
    """
    游戏对象实体对象
    """
    def __init__(self, entity_id):
        self._entity_id = entity_id

    @property
    def id(self):
        """ 返回游戏对象实体id
        """
        return self._entity_id

    def update(self):
        """ 实体对象更新方法
        """
        raise NotImplementedError

    def handle_message(self, telegram):
        """ 处理发送给本实体的消息
        """
        raise NotImplementedError

