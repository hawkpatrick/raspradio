import unittest

from root.raspradio.config import user_settings
from root.raspradio.config.stop_the_bell_settings import get_stop_the_bell_settings_from_config


class StopTheBellSettingsTest(unittest.TestCase):

    def test_get_settings_should_not_return_null_if_default_is_on(self):
        # given: Following setting is saved
        reqargs = {'SectionBellStopper_DefaultOn':'Yes', 'SectionBellStopper_DurationInMinutes':'2'}
        user_settings.save_user_settings(reqargs)
        # when
        stopTheBellSettings = get_stop_the_bell_settings_from_config()
        # then
        self.assertIsNotNone(stopTheBellSettings)
        assert stopTheBellSettings.turnOffAfterMinutes == 2

    def test_get_settings_should_return_none_if_default_is_off(self):
        # given: Following setting is saved
        reqargs = {'SectionBellStopper_DefaultOn':'No'}
        user_settings.save_user_settings(reqargs)
        # when
        settings = get_stop_the_bell_settings_from_config()
        # then
        assert settings == None
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()