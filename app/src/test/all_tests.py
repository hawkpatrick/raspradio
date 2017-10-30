'''
Created on 15.10.2017

@author: pho
'''
import unittest
from test.raspradio.streams_test import StreamsTest
from test.raspradio.radio_test import RadioTest
from test.raspradio.ring_alarm_test import RingAlarmTest
from test.raspradio.alarms_test import AlarmsTest
from test.raspradio.config.configuration_test import ConfigurationTest
from test.raspradio.control_vlc_test import ControlVlcTest
from test.raspradio.fade_in_test import FadeInTest


class Test(unittest.TestCase):


    def testName(self):
        pass


if __name__ == "__main__":
    suiteStreams = unittest.TestLoader().loadTestsFromTestCase(StreamsTest)
    suiteRadio = unittest.TestLoader().loadTestsFromTestCase(RadioTest)
    suiteAlarms = unittest.TestLoader().loadTestsFromTestCase(AlarmsTest)
    suiteRingAlarm = unittest.TestLoader().loadTestsFromTestCase(RingAlarmTest)
    suiteConfig = unittest.TestLoader().loadTestsFromTestCase(ConfigurationTest)
    suiteVlc = unittest.TestLoader().loadTestsFromTestCase(ControlVlcTest)
    suiteFadeIn = unittest.TestLoader().loadTestsFromTestCase(FadeInTest)

    allTests = unittest.TestSuite([
        suiteStreams, 
        suiteRadio, 
        suiteAlarms,
        suiteRingAlarm,
        suiteConfig,
        suiteVlc,
        suiteFadeIn
        ])
    unittest.TextTestRunner(verbosity=2).run(allTests)