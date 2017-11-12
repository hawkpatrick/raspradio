'''
Created on 04.11.2017

@author: pho
'''

from root.raspradio.alarms import alarm
from root.raspradio.bells import bell

import threading
from datetime import datetime
from dateutil import parser
from root.raspradio import alarms

def start_watching():
    t1 = threading.Thread(target=_watch_alarms_thread, args=[])
    t1.start()

def _watch_alarms_thread():
    for anAlarm in alarm.all_alarms:
        _evaluate_alarm(anAlarm)
    threading.Timer(5.0, _watch_alarms_thread).start()

def _evaluate_alarm(alarm):
    if not _must_ring_bell_now(alarm):
        return
    bell.activate_new_bell(alarm)
    if not alarm.repeat:
        alarm.isActive = False
        alarms.alarm.save_alarms_to_file()
     
def _must_ring_bell_now(alarm):
    now = _get_now()
    if alarm.hour != now.hour or alarm.minute != now.minute:
        return False
    if not alarm.isActive:
        return False
    if not alarm.repeat or not alarm.repeat.days:
        return True
    repeat = alarm.repeat
    weekdayNow = now.weekday()
    return weekdayNow in repeat.days

def _get_now():
    return datetime.now()
