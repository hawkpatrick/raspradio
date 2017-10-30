'''
Created on 30.10.2017

@author: pho
'''
import threading
from root.raspradio import control_vlc


def start_fade_in():
    fader = FadeIn(60, 256, 1)
    control_vlc.vlc_set_volume(0)
    print "Fade-In starting: From 0 to " + str(fader.targetVolume)

    t1 = threading.Thread(target=do_fade_in, args=[fader])
    t1.start()

def do_fade_in(fader):
    fader.currentVolume = fader.currentVolume + fader.deltaVolume
    if fader.currentVolume >= fader.targetVolume:
        print "Fade-In completed: Reached target volume of " + str(fader.targetVolume)
        fader.currentVolume = fader.targetVolume
    control_vlc.vlc_set_volume(fader.currentVolume)
    if fader.currentVolume < fader.targetVolume:
        threading.Timer(fader.deltaTime, do_fade_in, [fader]).start()

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
        self.timespan = timespan
        self.targetVolume = targetVolume
        self.deltaTime = deltaTime
        self.intervals = timespan / deltaTime
        self.deltaVolume = targetVolume / self.intervals
        self.currentVolume = 0
        


        