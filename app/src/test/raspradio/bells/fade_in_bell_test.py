'''
Created on 30.10.2017

@author: pho
'''
import unittest
from mock import patch
from root.raspradio.bells.fade_in_bell import FadeIn
from root.raspradio.bells import fade_in_bell
import threading


class FadeInTest(unittest.TestCase):

    @patch('root.raspradio.control_vlc.vlc_set_volume') 
    @patch.object(threading.Thread, 'start')  
    def testStartAndStopFader(self, mock_thread_start, mock_vlc_set_volume):
        fade_in_bell.create_new_fader()
        mock_vlc_set_volume.assert_called_once_with(0)
        mock_thread_start.assert_called_once()


    @patch('root.raspradio.control_vlc.vlc_set_volume') 
    @patch('root.raspradio.bells.fade_in_bell._repeat_fader_thread') 
    def testFader(self, mock_repeat_thread, mock_vlc_set_volume):
        timespan = 30
        targetVolume = 15
        intervalInSeconds = 10
        fader = FadeIn(timespan, targetVolume, intervalInSeconds)
        
        self.assertEquals(fade_in_bell.STATE_CREATED, fader.state)
        fader.activate()
        self.assertEquals(fade_in_bell.STATE_STARTED, fader.state)

        fade_in_bell._fader_thread(fader)
        mock_vlc_set_volume.assert_called_with(5)
        self.assertEquals(1, mock_repeat_thread.call_count)        

        fade_in_bell._fader_thread(fader)
        mock_vlc_set_volume.assert_called_with(10)
        self.assertEquals(2, mock_repeat_thread.call_count)
        
        fade_in_bell._fader_thread(fader)
        mock_vlc_set_volume.assert_called_with(15)
        self.assertEquals(3, mock_repeat_thread.call_count)
        
        self.assertEquals(fade_in_bell.STATE_STOPPED, fader.state)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FadeInTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 