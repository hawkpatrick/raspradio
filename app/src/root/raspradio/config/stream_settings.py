'''
Created on 25.11.2017

@author: pho
'''
from root.raspradio.config.user_settings import get_user_settings
        
class AlarmStreamSetting:
    def __init__(self, streamName):
        self.streamName = streamName
        

def get_default_stream_setting():
    streamName = get_user_settings()['SectionAlarmStreamSetting']['Stream']
    streamSetting = AlarmStreamSetting(streamName)
    return streamSetting