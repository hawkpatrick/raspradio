'''
Created on 04.11.2017

@author: pho
'''
from datetime import datetime
import fade_in_bell, stop_the_bell, play_music_of_bell

current_bell = None

def activate_new_bell(alarm):
    global current_bell
    if __is_current_active_bell_still_valid(alarm):
        return
    deactivate_current_bell()
    current_bell = Bell(alarm)
    current_bell.activate()

def deactivate_current_bell():
    if current_bell == None:
        return
    current_bell.deactivate()

def __is_current_active_bell_still_valid(alarm):
    now = datetime.now()
    if current_bell == None:
        return False
    timeActiveBell = current_bell.timeStarted
    delta = now - timeActiveBell
    return delta.seconds < 60 and current_bell.alarm.minute == alarm.minute
    

class Bell(object):
    '''
    classdocs
    '''

    def __init__(self, alarm):
        '''
        Constructor
        '''
        self.alarm = alarm
        self.fader = None
        self.stopper = None
        self.musicplayer = None
        self.isActive = False
        self.controlsLight = True
        self.controlsVolume = True
        self.controlsMusicplayer = True
        self.timeStarted = datetime.now()

        
    def activate(self):
        '''
        Starts ringing the bell which means playing the stream
        (triggered by alarm watch)
        '''
        print "Rining bell of alarm " + str(self.alarm)
        self.isActive = True
        self.__init_fader()
        self.__init_stopper()
        self.__init_musicplayer()
    
    def deactivate(self):
        '''
        Stops the bell from ringin (triggered by user input or by new bell)
        '''   
        self.isActive = False
        if self.fader != None: 
            self.fader.deactivate()
        if self.stopper != None: 
            self.stopper.deactivate()
        if self.musicplayer != None: 
            self.musicplayer.deactivate()

    def stop_controlling_volume(self):
        if self.fader != None:
            self.fader.deactivate()
        self.controlsVolume = False

    def __init_fader(self):
        if not self.alarm.isFadeInActive:
            return
        self.fader = fade_in_bell.create_new_fader()
        self.fader.activate()
        
    def __init_stopper(self):
        if self.alarm.bellDurationSeconds <= 0:
            return
        self.stopper = stop_the_bell.create_new_stop_the_bell(self.alarm)
        self.stopper.activate()
        
    def __init_musicplayer(self):
        self.musicplayer = play_music_of_bell.create_new_musicplayer(self.alarm)
        self.musicplayer.activate()
            
        
        
