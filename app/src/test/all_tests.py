import unittest
from unittest import TestLoader

from test.raspradio.config.fade_in_settings_test import FadeInSettingsTest
from test.raspradio.config.stop_the_bell_settings_test import StopTheBellSettingsTest
from test.raspradio.streams_test import StreamsTest
from test.raspradio.radio_test import RadioTest
from test.raspradio.alarms.alarm_test import AlarmTest
from test.raspradio.config.configuration_test import ConfigurationTest
from test.raspradio.control_vlc_test import ControlVlcTest
from test.raspradio.bells.fade_in_test import FadeInTest
from test.raspradio.bells.bells_test import BellTest
from test.raspradio.bells.stop_the_bell_test import StopTheBellTest
from test.raspradio.alarms.test_repeat_alarm import RepeatAlarmTest
from test.raspradio.alarms.watch_alarms_test import WatchAlarmTest



class Test(unittest.TestCase):


    def testName(self):
        pass

def __load_tests(clazz):
    return TestLoader().loadTestsFromTestCase(clazz)

if __name__ == "__main__":   
    allTests = unittest.TestSuite([
        __load_tests(StreamsTest), 
        __load_tests(RadioTest),
        __load_tests(AlarmTest),
        __load_tests(ConfigurationTest),
        __load_tests(ControlVlcTest),
        __load_tests(FadeInTest),
        __load_tests(BellTest),
        __load_tests(StopTheBellTest),
        __load_tests(RepeatAlarmTest),
        __load_tests(WatchAlarmTest),
        __load_tests(StopTheBellSettingsTest),
        __load_tests(FadeInSettingsTest)
        ])
    unittest.TextTestRunner(verbosity=2).run(allTests)