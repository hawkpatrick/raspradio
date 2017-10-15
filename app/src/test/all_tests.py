'''
Created on 15.10.2017

@author: pho
'''
import unittest
from test.raspradio.streams_test import StreamsTest
from test.raspradio.radio_test import RadioTest
from test.raspradio.ring_alarm_test import RingAlarmTest


class Test(unittest.TestCase):


    def testName(self):
        pass


if __name__ == "__main__":
    suiteStreams = unittest.TestLoader().loadTestsFromTestCase(StreamsTest)
    suiteRadio = unittest.TestLoader().loadTestsFromTestCase(RadioTest)
    suiteRingAlarm = unittest.TestLoader().loadTestsFromTestCase(RingAlarmTest)
    allTests = unittest.TestSuite([suiteStreams, suiteRadio, suiteRingAlarm])
    unittest.TextTestRunner(verbosity=2).run(allTests)