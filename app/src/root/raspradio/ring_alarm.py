'''
Created on 15.10.2017

@author: pho
'''
from datetime import datetime
from dateutil import parser
import streams, control_vlc
from root.raspradio.streams import play_stream

lastalarm = datetime.strptime('8/18/2008', "%m/%d/%Y")

def update_lastalarm(now):
    global lastalarm
    lastalarm = now

def must_evaluate_alarm(now):
    global lastalarm
    delta = now - lastalarm
    return delta.seconds > 60

def evaluate_alarm(alarm):
    now = datetime.now()
    if not must_evaluate_alarm(now):
        return
    line = "" + alarm.hour + ":" + alarm.minute
    alarmtime = parser.parse(line)
    if alarmtime.hour == now.hour and alarmtime.minute == now.minute:
        ring_ring(alarm)
        
def ring_ring(alarm): 
    print "Alarm!!!!"
    now = datetime.now()     
    if alarm.streamname:
        stream = streams.find_stream_by_name(alarm.streamname)
        if stream:
            play_stream(stream)
            update_lastalarm(now)
            return    
    control_vlc.vlccmd('pl_play')
    update_lastalarm(now)
