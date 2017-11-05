'''
Created on 05.11.2017

@author: pho
'''
import urllib 
from root.raspradio import streams, control_vlc

def create_new_musicplayer(alarm):
    result = Musicplayer(alarm)
    return result

class Musicplayer(object):
    '''
    classdocs
    '''


    def __init__(self, alarm):
        '''
        Constructor
        '''
        self.alarm = alarm
        
    def activate(self):
        if self.alarm.streamname:
            stream = streams.find_stream_by_name(self.alarm.streamname)
            if stream:
                encodedstream = urllib.quote_plus(stream.url)
                control_vlc.vlc_play_stream(encodedstream)
                return    
        control_vlc.vlccmd('pl_play')
        
    def deactivate(self):
        control_vlc.vlccmd('pl_pause')
