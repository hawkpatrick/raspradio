import unittest
from datetime import datetime

from mock import patch

from root.raspradio.alarms.alarm import Alarm
from root.raspradio.bells import bell
from root.raspradio.bells.bell_music_player import BellMusicPlayer


class BellTest(unittest.TestCase):

    def setUp(self):
        bell.active_bell = None


    @patch('root.raspradio.config.stop_the_bell_settings.get_stop_the_bell_settings_from_config')
    @patch.object(BellMusicPlayer, 'activate')  
    def testActivateBell(self, mock_activate, mock_get_stop_the_bell_settings):
        #given
        alarm = Alarm(1, 21, 54)
        alarm.stopTheBellSettings = None
        alarm.fadeInSetting = None
        mock_get_stop_the_bell_settings.return_value = None
        # when
        bell.activate_new_bell(alarm)
        # then
        self.assertIsNotNone(bell.current_bell)
        self.assertTrue(mock_activate.called)

    @patch('root.raspradio.config.stop_the_bell_settings.get_stop_the_bell_settings_from_config')
    @patch.object(BellMusicPlayer, 'activate')  
    def testActivateBellOnlyOnce(self, mock_activate, mock_get_stop_the_bell_settings):
        #given
        alarm1 = Alarm(1, 21, 54)
        alarm1.stopTheBellSettings = None
        alarm1.fadeInSetting = None
        alarm2 = Alarm(1, 21, 54)
        alarm2.stopTheBellSettings = None
        alarm2.fadeInSetting = None
        bell.activate_new_bell(alarm1)
        bell1 = bell.current_bell
        mock_get_stop_the_bell_settings.return_value = None
        # when
        bell.activate_new_bell(alarm2)
        # then
        self.assertEqual(bell.current_bell, bell1)

    @patch('root.raspradio.config.stop_the_bell_settings.get_stop_the_bell_settings_from_config')
    @patch.object(BellMusicPlayer, 'activate')  
    def testActivatingNewBellTurnsOffCurrentBell(self, mock_activate, mock_get_stop_the_bell_settings):
        #given
        alarm1 = Alarm(1, 21, 54)
        alarm1.stopTheBellSettings = None
        alarm1.fadeInSetting = None
        theBell = bell.Bell(alarm1)
        theBell.timeStarted = datetime.strptime('8/18/2008', "%m/%d/%Y")
        bell.current_bell = theBell
        alarm2 = Alarm(1, 22, 54)
        alarm2.stopTheBellSettings = None
        alarm2.fadeInSetting = None
        mock_get_stop_the_bell_settings.return_value = None
        # when
        bell.activate_new_bell(alarm2)
        # then
        self.assertFalse(theBell.isActive)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()    
