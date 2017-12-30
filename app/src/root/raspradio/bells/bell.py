from datetime import datetime
import fade_in, stop_the_bell, bell_music_player
from root.raspradio.config import fade_in_settings
from root.raspradio.config import stop_the_bell_settings
from root.raspradio.config import stream_settings
import time

current_bell = None


def activate_new_bell(alarm):
    global current_bell
    if _is_current_active_bell_still_valid(alarm):
        return
    _deactivate_current_bell()
    current_bell = Bell(alarm)
    _activate_current_bell()


def remove_player_control_from_current_bell():
    """
    When there is user input the current bell is not allowed to do anything anymore!
    """
    if current_bell is None:
        return
    current_bell.stop_controlling_player()


def remove_volume_control_from_current_bell():
    if current_bell is None:
        return
    current_bell.stop_controlling_volume()


def _deactivate_current_bell():
    if current_bell is None:
        return
    current_bell.deactivate()


def _activate_current_bell():
    if current_bell is None:
        return
    current_bell.activate()


def _is_current_active_bell_still_valid(alarm):
    now = datetime.now()
    if current_bell is None:
        return False
    timeActiveBell = current_bell.timeStarted
    delta = now - timeActiveBell
    return delta.seconds < 60 and current_bell.alarm.minute == alarm.minute
    

class Bell(object):

    def __init__(self, alarm):
        self.alarm = alarm
        self.fader = None
        self.stopTheBell = None
        self.musicplayer = None
        self.isActive = False
        self.timeStarted = datetime.now()
        self.controlsVolume = True
        self.controlsMusicPlayer = True

    def activate(self):
        """
        Starts ringing the bell which means playing the stream
        (triggered by alarm watch)
        """
        print "Rining bell of alarm " + str(self.alarm)
        self.isActive = True
        self.__init_fader()
        self.__init_stop_the_bell()
        self.__init_musicplayer()
    
    def deactivate(self):
        """
        Stops the bell from ringin (triggered by user input or by new bell or by stopTheBell)
        """
        self.isActive = False
        if self.fader is not None:
            self.fader.deactivate_fade_in()
        if self.stopTheBell is not None:
            self.stopTheBell.deactivate_stop_the_bell()
        if self.musicplayer is not None:
            self.musicplayer.deactivate_bell_music_player()

    def stop_controlling_volume(self):
        if self.fader is not None:
            self.fader.deactivate_fade_in()
        self.controlsVolume = False

    def stop_controlling_player(self):
        if self.stopTheBell is not None:
            self.stopTheBell.deactivate_stop_the_bell()
        self.controlsMusicPlayer = False

    def __init_fader(self):
        fadeInSettings = self.__get_fader_settings()
        if not fadeInSettings:
            return
        self.fader = fade_in.create_new_fader(fadeInSettings)
        self.fader.activate_fade_in()
        
    def __init_stop_the_bell(self):
        stopBellSettings = self.__get_stop_the_bell_settings()
        if not stopBellSettings:
            return
        self.stopTheBell = stop_the_bell.create_new_stop_the_bell(stopBellSettings, self)
        self.stopTheBell.activate_stop_the_bell()
        
    def __init_musicplayer(self):
        streamSetting = self.__get_stream_setting()
        self.musicplayer = bell_music_player.create_new_musicplayer(streamSetting)
        time.sleep(2)
        self.musicplayer.activate_bell_music_player()
        
    def __get_fader_settings(self):
        if self.alarm.fadeInSetting:
            return self.alarm.fadeInSetting
        return fade_in_settings.get_fade_in_settings_from_config()   
    
    def __get_stop_the_bell_settings(self):
        if self.alarm.stopTheBellSettings:
            return self.alarm.stopTheBellSettings
        return stop_the_bell_settings.get_stop_the_bell_settings_from_config()
    
    def __get_stream_setting(self):
        if self.alarm.streamSetting:
            return self.alarm.streamSetting
        return stream_settings.get_default_stream_setting()
