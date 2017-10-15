'''
Created on 15.10.2017

@author: pho
'''
import unittest
from root.raspradio import radio
from root.raspradio.radio import Alarm

class RadioTest(unittest.TestCase):


    def setUp(self):
        radio.alarms = []
        assert len(radio.alarms) is 0

    def tearDown(self):
        pass


    def test_add_new_alarm(self):
        assert len(radio.alarms) is 0
        alarm = Alarm("1", "10", "22")
        radio.add_new_alarm(alarm)
        assert len(radio.alarms) is 1


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_upper']
    suite = unittest.TestLoader().loadTestsFromTestCase(RadioTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 
    
    
