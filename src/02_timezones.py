#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:05:01 2021

@author: flonblnx
"""
from datetime import datetime
from zoneinfo import ZoneInfo

now_Pacific = datetime.now(ZoneInfo('America/Los_Angeles'))
print(f"current Pacific time: {now_Pacific.isoformat(timespec='seconds')}")
# current Pacific time: 2021-10-17T01:19:22-07:00

print(now_Pacific.tzinfo, now_Pacific.utcoffset())
# America/Los_Angeles -1 day, 17:00:00


now_UTC = now_Pacific.astimezone(ZoneInfo("UTC"))
print(f"current UTC time: {now_UTC.isoformat(timespec='seconds')}")
# current UTC time: 2021-10-17T08:19:22+00:00



summer = datetime(2021, 10, 31, tzinfo=ZoneInfo("Europe/Berlin"))
winter = datetime(2021, 11, 1, tzinfo=ZoneInfo("Europe/Berlin"))
print(f"summer time: {summer.isoformat()}")
print(f"winter time: {winter.isoformat()}")
# summer time: 2021-10-31T00:00:00+02:00
# winter time: 2021-11-01T00:00:00+01:00



naive = datetime(2021, 10, 17) # this should be in time zone Europe/Berlin...
print(naive)
# 2021-10-17 00:00:00
aware = naive.replace(tzinfo=ZoneInfo("Europe/Berlin"))
print(aware)
# 2021-10-17 00:00:00+02:00