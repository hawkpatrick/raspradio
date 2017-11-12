'''
Created on 05.11.2017

@author: pho
'''
import configuration

def get_fader_timespan():
    return configuration.read_config_value_as_int("SectionBellFader", "Timespan")
    
def get_fader_target_volume():
    return configuration.read_config_value_as_int("SectionBellFader", "TargetVolume")
    
def get_fader_delta_time():
    return configuration.read_config_value_as_int("SectionBellFader", "DeltaTime")

def get_stopper_duration_in_minutes():
    return configuration.read_config_value_as_int("SectionBellStopper", "DurationInMinutes")