import urllib
from root.raspradio import streams
from root.raspradio.vlc import control_vlc


def create_new_musicplayer(streamSetting):
    result = BellMusicPlayer(streamSetting)
    return result


class BellMusicPlayer(object):

    def __init__(self, streamSetting):
        self.streamSetting = streamSetting
        
    def activate_bell_music_player(self):
        if self.streamSetting:
            stream = streams.find_stream_by_name(self.streamSetting.streamName)
            if stream:
                encodedstream = urllib.quote_plus(stream.url)
                control_vlc.vlc_play_stream(encodedstream)
                return    
        control_vlc.vlc_resume()
        
    def deactivate_bell_music_player(self):
        control_vlc.vlc_pause()
