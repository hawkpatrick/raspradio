'''
Created on 04.11.2017

@author: pho
'''
from datetime import datetime
import fade_in_bell, stop_the_bell, play_music_of_bell
from root.raspradio.config import fade_in_settings
from root.raspradio.config import turn_off_settings
from root.raspradio.config import stream_settings

current_bell = None

def activate_new_bell(alarm):
    global current_bell
    if _is_current_active_bell_still_valid(alarm):
        return
    _deactivate_current_bell()
    current_bell = Bell(alarm)
    _activate_current_bell()

def _deactivate_current_bell():
    if current_bell == None:
        return
    current_bell.deactivate()
    
def _activate_current_bell():
    if current_bell == None:
        return
    current_bell.activate()
    
def _is_current_active_bell_still_valid(alarm):
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
        fadeInSettings = self.__get_fader_settings()
        if not fadeInSettings.active:
            return
        self.fader = fade_in_bell.create_new_fader()
        self.fader.activate()
        
    def __init_stopper(self):
        turnOffSettings = self.__get_turn_off_settings()
        if not turnOffSettings:
            return
        self.stopper = stop_the_bell.create_new_stopper(self.alarm.turnOffSetting)
        self.stopper.activate()
        
    def __init_musicplayer(self):
        streamSetting = self.__get_stream_setting()
        self.musicplayer = play_music_of_bell.create_new_musicplayer(streamSetting)
        self.musicplayer.activate()
        
    def __get_fader_settings(self):
        if self.alarm.fadeInSetting:
            return self.alarm.fadeInSetting
        return fade_in_settings.get_default()   
    
    def __get_turn_off_settings(self):
        if self.alarm.turnOffSetting:
            self.alarm.turnOffSetting
        return turn_off_settings.get_default()
    
    def __get_stream_setting(self):
        if self.alarm.streamSetting:
            return self.alarm.streamSetting
        return stream_settings.get_default_stream_setting()
        
        
