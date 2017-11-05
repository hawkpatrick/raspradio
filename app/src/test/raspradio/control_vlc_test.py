'''
Created on 30.10.2017

@author: pho
'''
import unittest
from root.raspradio import control_vlc
from mock import patch


class ControlVlcTest(unittest.TestCase):
    
    @patch('root.raspradio.control_vlc.vlc_set_volume')
    @patch('root.raspradio.control_vlc.vlc_read_volume')
    def testIncreaseVolume(self, mock_vlc_read_volume, mock_vlc_set_volume):
        mock_vlc_read_volume.return_value = 20
        control_vlc.vlc_increase_volume(10)
        mock_vlc_set_volume.assert_called_with(30)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_upper']
    suite = unittest.TestLoader().loadTestsFromTestCase(ControlVlcTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 