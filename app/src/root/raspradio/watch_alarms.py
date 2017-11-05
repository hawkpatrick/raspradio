'''
Created on 04.11.2017

@author: pho
'''

import alarms
from bell import bells

import threading
from datetime import datetime
from dateutil import parser

def start_watching():
    t1 = threading.Thread(target=__watch_alarms_thread, args=[])
    t1.start()

def __watch_alarms_thread():
    for alarm in alarms.all_alarms:
        evaluate_alarm(alarm)
    threading.Timer(5.0, __watch_alarms_thread).start()

def evaluate_alarm(alarm):
    now = datetime.now()
    line = "" + alarm.hour + ":" + alarm.minute
    alarmtime = parser.parse(line)
    if alarmtime.hour == now.hour and alarmtime.minute == now.minute:
        ring_ring(alarm)
        
        
def ring_ring(alarm): 
    bells.activate_new_bell(alarm)
    
    