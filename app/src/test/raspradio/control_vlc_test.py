'''
Created on 30.10.2017

@author: pho
'''
import unittest
from root.raspradio import control_vlc


class ControlVlcTest(unittest.TestCase):


    def testName(self):
        control_vlc.vlc_read_volume()
        pass
    
    def testIncreaseVolume(self):
        control_vlc.vlc_increase_volume(10)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_upper']
    suite = unittest.TestLoader().loadTestsFromTestCase(ControlVlcTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 