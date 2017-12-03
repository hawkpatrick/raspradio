'''
Created on 30.10.2017

@author: pho
'''
import threading
from root.raspradio import control_vlc
from root.raspradio.config import bell_config
    
STATE_CREATED = 1
STATE_STARTED = 2
STATE_STOPPED = 3

def create_new_fader():
    control_vlc.vlc_set_volume(0)
    timespan = bell_config.get_fader_timespan()
    targetVolume = bell_config.get_fader_target_volume()
    deltaTime = bell_config.get_fader_delta_time()
    fader = FadeIn(timespan, targetVolume, deltaTime)
    print "Fade-In starting: From 0 to " + str(fader.targetVolume)
    _start_fader_thread(fader)
    return fader

def _start_fader_thread(fader):
    faderThread = threading.Thread(target=_fader_thread, args=[fader])
    faderThread.start()
    
def _repeat_fader_thread(fader):     
    if fader.state == STATE_STOPPED:
        return
    t = threading.Timer(fader.deltaTime, _fader_thread, [fader])
    t.start()
    
def _fader_thread(fader):
    fader.currentVolume = fader.currentVolume + fader.deltaVolume
    if fader.currentVolume >= fader.targetVolume:
        print "Fade-In completed: Reached target volume of " + str(fader.targetVolume)
        fader.currentVolume = fader.targetVolume
        fader.deactivate()
    control_vlc.vlc_set_volume(fader.currentVolume)   
    _repeat_fader_thread(fader)
    

        
    
    

class FadeIn(object):
    '''
    Args:
        stream
        timespan
        targetVolume
        deltaTime Time in seconds for interval between volume increasing events
    '''

    def __init__(self, timespan, targetVolume, deltaTime):
        '''
        Constructor
        '''
        self.state = STATE_CREATED
        self.timespan = timespan
        self.targetVolume = targetVolume
        self.deltaTime = deltaTime
        self.intervals = timespan / deltaTime
        self.deltaVolume = targetVolume / self.intervals
        self.currentVolume = 0
        
    def activate(self):
        self.state = STATE_STARTED
    
    def deactivate(self):
        self.state = STATE_STOPPED

        