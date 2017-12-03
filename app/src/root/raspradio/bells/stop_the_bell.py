'''
Created on 05.11.2017

@author: pho
'''
import threading
from datetime import datetime
from root.raspradio import control_vlc

STATE_CREATED = 0
STATE_RUNNING = 1
STATE_STOPPED = 2

MONITOR_INTERVAL_IN_SECONDS = 10

def create_new_stopper(turnOffSetting):
    stopper = Stopper(turnOffSetting.turnOffAfterSeconds)
    _start_stop_bell_monitor_thread(stopper)
    return stopper

def _start_stop_bell_monitor_thread(stopper):
    faderThread = threading.Thread(target=_stop_bell_monitor_thread, args=[stopper])
    faderThread.start()

def _repeat_stop_bell_monitor_thread(stopper):
    if stopper.state == STATE_STOPPED:
        return
    t = threading.Timer(MONITOR_INTERVAL_IN_SECONDS, _stop_bell_monitor_thread, [stopper])
    t.start()
        
def _stop_bell_monitor_thread(stopper):
    if stopper.mustStopTheBellNow():
        stopper.stopTheBellNow()
    _repeat_stop_bell_monitor_thread(stopper)

class Stopper(object):
    '''
    classdocs
    '''

    def __init__(self, bellDurationSeconds):
        '''
        Constructor
        '''
        self.state = STATE_CREATED
        self.bellDurationSeconds = bellDurationSeconds
        self.timeStarted = datetime.now()
        
    def activate(self):
        self.state = STATE_RUNNING
        
    def deactivate(self):
        self.state = STATE_STOPPED
        
    def mustStopTheBellNow(self):
        now = datetime.now()
        durationSoFar = now - self.timeStarted
        return durationSoFar.seconds >= self.bellDurationSeconds
    
    def stopTheBellNow(self):
        if self.state != STATE_RUNNING:
            return
        control_vlc.vlccmd('pl_pause')

        
    
        