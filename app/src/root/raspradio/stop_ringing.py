'''
Created on 30.10.2017

@author: pho
'''

import threading, control_vlc
from datetime import datetime

current_alarm = None

def start_timer_stop_ringing(alarm):
    global current_alarm
    current_alarm = alarm
    if alarm.duration <= 0:
        return
    current_alarm.startedAt = datetime.now().total_seconds()
    t1 = threading.Thread(target=event_check_stop_ringing, args=[alarm])
    t1.start()    
    
def event_check_stop_ringing(alarm):
    if current_alarm.alarmid != alarm.alarmid:
        return
    now = datetime.now().total_seconds()
    delta = now - current_alarm.startedAt
    if delta > current_alarm.duration:
        do_stop()
        return
    threading.Timer(10.0, event_check_stop_ringing, [alarm]).start()
    
def do_stop():
    print "Stopping alarm: duration exceeded"
    control_vlc.vlccmd('pl_pause')
    pass
