import unittest
from root.raspradio.alarms import repeat_alarm


class RepeatAlarmTest(unittest.TestCase):


    def test_create_repeat_from_dict_none(self):
        result = repeat_alarm.create_repeat_from_dict(None)
        self.assertIsNone(result)


    def test_create_repeat_from_dict_empy(self):
        dct = {}
        result = repeat_alarm.create_repeat_from_dict(dct)
        self.assertIsNone(result)
    
    def test_create_repeat_from_dict_valid(self):
        dct = {'days': [4, 5]}
        result = repeat_alarm.create_repeat_from_dict(dct)
        self.assertIsNotNone(result)
        self.assertEquals(2, len(result.days))
        self.assertEquals(4, result.days[0])
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()