import unittest
from mock import patch
from root.raspradio.bells.fade_in import FadeIn
from root.raspradio.bells import fade_in
import threading

from root.raspradio.config.fade_in_settings import FadeInSettings


class FadeInTest(unittest.TestCase):

    @patch('root.raspradio.control_vlc.vlc_set_volume') 
    @patch.object(threading.Thread, 'start')  
    def testStartAndStopFader(self, mock_thread_start, mock_vlc_set_volume):
        # given
        fadeInSettings = FadeInSettings(10)
        # when
        fade_in.create_new_fader(fadeInSettings)
        # then
        mock_vlc_set_volume.assert_called_once_with(0)
        mock_thread_start.assert_called_once()


    @patch('root.raspradio.control_vlc.vlc_set_volume') 
    @patch('root.raspradio.bells.fade_in._repeat_fader_thread')
    def testFader(self, mock_repeat_thread, mock_vlc_set_volume):
        timespanInSeconds = 30
        targetVolume = 15
        intervalInSeconds = 10
        fader = FadeIn(timespanInSeconds, targetVolume, intervalInSeconds)
        
        self.assertEquals(fade_in.STATE_CREATED, fader.state)
        fader.activate()
        self.assertEquals(fade_in.STATE_STARTED, fader.state)

        fade_in._fader_thread(fader)
        mock_vlc_set_volume.assert_called_with(5)
        self.assertEquals(1, mock_repeat_thread.call_count)        

        fade_in._fader_thread(fader)
        mock_vlc_set_volume.assert_called_with(10)
        self.assertEquals(2, mock_repeat_thread.call_count)
        
        fade_in._fader_thread(fader)
        mock_vlc_set_volume.assert_called_with(15)
        self.assertEquals(3, mock_repeat_thread.call_count)
        
        self.assertEquals(fade_in.STATE_STOPPED, fader.state)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FadeInTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 