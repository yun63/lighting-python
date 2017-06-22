# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: time_unittest.py

@Description:

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-06-19 17:27:02

"""

import time
from datetime import datetime
import unittest

import util.time_util as lttime


class TimeUtilTest(unittest.TestCase):

    def setUp(self):
        self.date_str = '2017-06-19 12:30:30'
        self.dt = datetime(year=2017, month=06, day=19, hour=12, minute=30, second=30)
        self.t = self.dt.timetuple()
        self.ts = int(time.mktime(self.t))
        self.format = '%Y-%m-%d %H:%M:%S'

    def tearDown(self):
        pass

    def test_current_timestamp(self):
        pass

    def test_from_timestr(self):
        self.assertEqual(lttime.from_timestr(self.date_str, self.format), self.dt)

    def test_to_timestr(self):
        self.assertEqual(lttime.to_timestr(self.dt, self.format), self.date_str)

    def test_seconds_diff(self):
        other_date_str = '2017-06-19 13:30:30'
        self.assertEqual(lttime.seconds_diff(self.date_str, other_date_str), 3600)

    def test_from_timestamp(self):
        self.assertEqual(lttime.from_timestamp(self.ts), self.dt)

    def test_datetime_to_timestamp(self):
        self.assertEqual(lttime.datetime_to_timestamp(self.dt), self.ts)

    def test_strtime_to_timestamp(self):
        self.assertEqual(lttime.strtime_to_timestamp(self.date_str), self.ts)

    def test_is_same_day(self):
        other_date_str = '2017-06-19 13:30:30'
        self.assertEqual(lttime.is_same_day(self.date_str, other_date_str), True)
        other_dt = datetime(year=2017, month=06, day=19, hour=19, minute=30, second=30)
        self.assertEqual(lttime.is_same_day(self.dt, other_dt), True)


if __name__ == '__main__':
    unittest.main()
