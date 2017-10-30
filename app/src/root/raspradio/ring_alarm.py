'''
Created on 15.10.2017

@author: pho
'''
from datetime import datetime
from dateutil import parser
import streams, control_vlc, urllib, fade_in, stop_ringing

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
            encodedstream = urllib.quote_plus(stream.url)
            if alarm.fadein:
                fade_in.start_fade_in()
            control_vlc.vlc_play_stream(encodedstream)
            stop_ringing.start_timer_stop_ringing(alarm)
            update_lastalarm(now)
            return    
    control_vlc.vlccmd('pl_play')
    update_lastalarm(now)
    
