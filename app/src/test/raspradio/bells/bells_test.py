'''
Created on 04.11.2017

@author: pho
'''
import unittest
from mock import patch

from root.raspradio.bells import bell
from root.raspradio.alarms.alarm import Alarm
from datetime import datetime
from root.raspradio.bells.play_music_of_bell import Musicplayer


class BellTest(unittest.TestCase):

    def setUp(self):
        bell.active_bell = None
        
    @patch.object(Musicplayer, 'activate')  
    def testActivateBell(self, mock_activate):
        #given
        alarm = Alarm(1, 21, 54)
        alarm.bellDurationSeconds = 0
        alarm.isFadeInActive = False
        # when
        bell.activate_new_bell(alarm)
        # then
        self.assertIsNotNone(bell.current_bell)
        self.assertTrue(mock_activate.called)

    @patch.object(Musicplayer, 'activate')  
    def testActivateBellOnlyOnce(self, mock_activate):
        #given
        alarm1 = Alarm(1, 21, 54)
        alarm1.bellDurationSeconds = 0   
        alarm1.isFadeInActive = False
        alarm2 = Alarm(1, 21, 54)
        alarm2.bellDurationSeconds = 0  
        alarm2.isFadeInActive = False 
        bell.activate_new_bell(alarm1)
        bell1 = bell.current_bell
        # when
        bell.activate_new_bell(alarm2)
        # then
        self.assertEqual(bell.current_bell, bell1)

    @patch.object(Musicplayer, 'activate')  
    def testActivatingNewBellTurnsOffCurrentBell(self, mock_activate):
        #given
        alarm1 = Alarm(1, 21, 54)
        alarm1.bellDurationSeconds = 0   
        alarm1.isFadeInActive = False
        theBell = bell.Bell(alarm1)
        theBell.timeStarted = datetime.strptime('8/18/2008', "%m/%d/%Y")
        bell.current_bell = theBell
        alarm2 = Alarm(1, 22, 54)
        alarm2.bellDurationSeconds = 0   
        alarm2.isFadeInActive = False
        # when
        bell.activate_new_bell(alarm2)
        # then
        self.assertFalse(theBell.isActive)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()    
