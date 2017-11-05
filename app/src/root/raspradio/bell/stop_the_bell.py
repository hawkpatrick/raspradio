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

STOP_BELL_MONITOR_INTERVAL = 10

def create_new_stop_the_bell(alarm):
    result = Stopper(alarm.bellDurationSeconds)
    faderThread = threading.Thread(target=__stop_bell_thread, args=[result])
    faderThread.start()
    return result

def __stop_bell_thread(stopTheBell):
    if stopTheBell.mustStopTheBellNow():
        stopTheBell.stopTheBellNow()
    if stopTheBell.state != STATE_STOPPED:
        threading.Timer(STOP_BELL_MONITOR_INTERVAL, __stop_bell_thread, [stopTheBell]).start()

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

        
    
        