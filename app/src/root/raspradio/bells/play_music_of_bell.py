'''
Created on 05.11.2017

@author: pho
'''
import urllib 
from root.raspradio import streams, control_vlc

def create_new_musicplayer(streamSetting):
    result = BellMusicPlayer(streamSetting)
    return result

class BellMusicPlayer(object):
    '''
    classdocs
    '''

    def __init__(self, streamSetting):
        '''
        Constructor
        '''
        self.streamSetting = streamSetting
        
    def activate(self):
        if self.streamSetting:
            stream = streams.find_stream_by_name(self.streamSetting.streamName)
            if stream:
                encodedstream = urllib.quote_plus(stream.url)
                control_vlc.vlc_play_stream(encodedstream)
                return    
        control_vlc.vlccmd('pl_play')
        
    def deactivate(self):
        control_vlc.vlccmd('pl_pause')
        
