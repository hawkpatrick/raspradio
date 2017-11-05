'''
Created on 30.10.2017

@author: pho
'''
import unittest
from mock import patch
from root.raspradio.bell.fade_in_bell import create_new_fader, FadeIn
from root.raspradio.bell import fade_in_bell


class FadeInTest(unittest.TestCase):

    @patch('root.raspradio.control_vlc.vlc_set_volume')
    def testStartAndStopFader(self, mock_vlc_set_volume):
        fader = FadeIn(10, 100, 1)
        fade_in_bell.__fade_in_loop_thread(fader)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FadeInTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 