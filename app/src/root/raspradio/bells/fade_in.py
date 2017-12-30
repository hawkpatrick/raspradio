import threading
from root.raspradio.vlc import control_vlc

STATE_CREATED = 1
STATE_STARTED = 2
STATE_STOPPED = 3

# Target volume for the fader. 256 means 100%
FADE_IN_TARGET_VOLUME = 256

# Indicates after how many seconds the volume should be increased
FADE_IN_INTERVAL_TIME_IN_SECONDS = 2


def create_new_fader(fadeInSettings):
    control_vlc.vlc_set_volume(0)
    targetVolume = FADE_IN_TARGET_VOLUME
    deltaTime = FADE_IN_INTERVAL_TIME_IN_SECONDS
    fader = FadeIn(fadeInSettings.durationInSeconds, targetVolume, deltaTime)
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
    if fader.state == STATE_STOPPED:
        return
    fader.currentVolume = fader.currentVolume + fader.deltaVolume
    if fader.currentVolume >= fader.targetVolume:
        print "Fade-In completed: Reached target volume of " + str(fader.targetVolume)
        fader.currentVolume = fader.targetVolume
        fader.deactivate()
    control_vlc.vlc_set_volume(fader.currentVolume)   
    _repeat_fader_thread(fader)


class FadeIn(object):

    def __init__(self, timespanInSeconds, targetVolume, deltaTime):
        self.state = STATE_CREATED
        self.timespan = timespanInSeconds
        self.targetVolume = targetVolume
        self.deltaTime = deltaTime
        self.intervals = timespanInSeconds / deltaTime
        self.deltaVolume = targetVolume / self.intervals
        self.currentVolume = 0
        
    def activate_fade_in(self):
        self.state = STATE_STARTED
    
    def deactivate_fade_in(self):
        self.state = STATE_STOPPED