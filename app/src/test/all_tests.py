'''
Created on 15.10.2017

@author: pho
'''
import unittest
from unittest import TestLoader
from test.raspradio.streams_test import StreamsTest
from test.raspradio.radio_test import RadioTest
from test.raspradio.alarms_test import AlarmsTest
from test.raspradio.config.configuration_test import ConfigurationTest
from test.raspradio.control_vlc_test import ControlVlcTest
from test.raspradio.bells.fade_in_bell_test import FadeInTest
from test.raspradio.bells.bell_test import BellTest
from test.raspradio.bells.stop_the_bell_test import StopTheBellTest



class Test(unittest.TestCase):


    def testName(self):
        pass

def __load_tests(clazz):
    return TestLoader().loadTestsFromTestCase(clazz)

if __name__ == "__main__":   
    allTests = unittest.TestSuite([
        __load_tests(StreamsTest), 
        __load_tests(RadioTest),
        __load_tests(AlarmsTest),
        __load_tests(ConfigurationTest),
        __load_tests(ControlVlcTest),
        __load_tests(FadeInTest),
        __load_tests(BellTest),
        __load_tests(StopTheBellTest)

        ])
    unittest.TextTestRunner(verbosity=2).run(allTests)