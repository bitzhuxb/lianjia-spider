#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import pytz
class TimeUtli:
    @staticmethod
    def get_utc_date_from_timestamp(timestamp):
        t1 = datetime.fromtimestamp(timestamp, pytz.timezone('UTC'))
        t1 = t1.date().__str__()
        return t1

