import unittest
from root.raspradio.alarms import alarm


class AlarmTest(unittest.TestCase):

    def setUp(self):
        alarm.all_alarms = []
        assert len(alarm.all_alarms) is 0

    def tearDown(self):
        alarm.save_alarms_to_file()


    def test_add_new_alarm(self):
        assert len(alarm.all_alarms) is 0
        reqargs = { "hour": "01", 
                   "minute" : "10", 
                   "stream" : "anystream"}
        alarm.add_alarm_by_request_args(reqargs)
        assert len(alarm.all_alarms) is 1
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()