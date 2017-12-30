import threading
from datetime import datetime

STATE_CREATED = 0
STATE_RUNNING = 1
STATE_STOPPED = 2

# Alle X Sekunden wird gecheckt, ob die Bell gestoppt werden soll
MONITOR_INTERVAL_IN_SECONDS = 10

def create_new_stop_the_bell(stopTheBellSettings, bell):
    stopTheBell = StopTheBell(bell, stopTheBellSettings.turnOffAfterMinutes * 60)
    _start_stop_bell_monitor_thread(stopTheBell)
    return stopTheBell

def _start_stop_bell_monitor_thread(stopTheBell):
    faderThread = threading.Thread(target=_stop_bell_monitor_thread, args=[stopTheBell])
    faderThread.start()

def _repeat_stop_bell_monitor_thread(stopTheBell):
    if stopTheBell.state == STATE_STOPPED:
        return
    t = threading.Timer(MONITOR_INTERVAL_IN_SECONDS, _stop_bell_monitor_thread, [stopTheBell])
    t.start()
        
def _stop_bell_monitor_thread(stopTheBell):
    if stopTheBell.mustStopTheBellNow():
        stopTheBell.stopTheBellNow()
    _repeat_stop_bell_monitor_thread(stopTheBell)

class StopTheBell(object):

    def __init__(self, bell, bellDurationSeconds):
        self.state = STATE_CREATED
        self.bell = bell
        self.bellDurationSeconds = bellDurationSeconds
        self.timeStarted = datetime.now()
        
    def activate_stop_the_bell(self):
        self.state = STATE_RUNNING
        
    def deactivate_stop_the_bell(self):
        self.state = STATE_STOPPED
        
    def mustStopTheBellNow(self):
        now = datetime.now()
        durationSoFar = now - self.timeStarted
        return durationSoFar.seconds >= self.bellDurationSeconds
    
    def stopTheBellNow(self):
        if self.state != STATE_RUNNING:
            return
        self.bell.deactivate()