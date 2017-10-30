'''
Created on 19.10.2017

@author: pho
'''
import unittest
from root.raspradio import alarms


class AlarmsTest(unittest.TestCase):

    def setUp(self):
        alarms.all_alarms = []
        assert len(alarms.all_alarms) is 0

    def tearDown(self):
        alarms.save_alarms_to_file()


    def test_add_new_alarm(self):
        assert len(alarms.all_alarms) is 0
        alarms.add_new_alarm("1", "10", "22", True)
        assert len(alarms.all_alarms) is 1
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()