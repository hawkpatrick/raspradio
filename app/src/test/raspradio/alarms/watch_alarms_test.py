import unittest
from root.raspradio.alarms import watch_alarms
from root.raspradio.alarms.alarm import Alarm
from mock import patch
from dateutil import parser
from root.raspradio.alarms.repeat_alarm import RepeatAlarm


def mock_get_now():
    '''
    Mock which in these tests is returned when calling datetime.now()
    '''
    return parser.parse("Mon Feb 15 2010 10:00")
    
class WatchAlarmTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    @patch('root.raspradio.alarms.watch_alarms._get_now', mock_get_now)
    def test_must_ring_bell_wrong_time(self):
        '''
        This should return false as the alarm time is not now (now is mocked).
        '''
        # given: an alarm at 11:00
        alarm = Alarm(0, 11, 00)
        # when: checking if alarm must ring bell
        result = watch_alarms._must_ring_bell_now(alarm)
        # then: false, as (mocked) now is not 11:00
        self.assertFalse(result)
            
    @patch('root.raspradio.alarms.watch_alarms._get_now', mock_get_now)
    def test_must_ring_bell_now_no_repeat(self):
        alarm = Alarm(0, 10, 00)
        result = watch_alarms._must_ring_bell_now(alarm)
        self.assertTrue(result)

    @patch('root.raspradio.alarms.watch_alarms._get_now', mock_get_now)
    def test_must_ring_bell_now_not_active(self):
        # given
        alarm = Alarm(0, 10, 00)
        alarm.isActive = False
        # when
        result = watch_alarms._must_ring_bell_now(alarm)
        # then
        self.assertFalse(result)
        
    @patch('root.raspradio.alarms.watch_alarms._get_now', mock_get_now)
    def test_must_ring_bell_now_monday_positive(self):
        # given
        alarm = Alarm(0, 10, 00)
        repetition = RepeatAlarm()
        repetition.days = [0]
        alarm.repetition = repetition
        # when
        result = watch_alarms._must_ring_bell_now(alarm)
        # then
        self.assertTrue(result)
             
    @patch('root.raspradio.alarms.watch_alarms._get_now', mock_get_now)
    def test_must_ring_bell_now_monday_negative(self):
        # given
        alarm = Alarm(0, 10, 00)
        repetition = RepeatAlarm()
        repetition.days = [1]
        alarm.repetition = repetition
        # when
        result = watch_alarms._must_ring_bell_now(alarm)
        # then
        self.assertFalse(result)   
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()