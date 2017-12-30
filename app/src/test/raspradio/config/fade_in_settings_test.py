import unittest

from root.raspradio.config import user_settings
from root.raspradio.config.fade_in_settings import get_fade_in_settings_from_config


class FadeInSettingsTest(unittest.TestCase):

    def test_get_settings_should_not_return_null_if_default_is_on(self):
        # given: Following setting is saved
        reqargs = {'SectionBellFader_DefaultOn':'Yes', 'SectionBellFader_TimespanInSeconds':'2'}
        user_settings.save_user_settings(reqargs)
        # when
        fadeInSettings = get_fade_in_settings_from_config()
        # then
        self.assertIsNotNone(fadeInSettings)
        assert fadeInSettings.durationInSeconds == 2

    def test_get_settings_should_return_none_if_default_is_off(self):
        # given: Following setting is saved
        reqargs = {'SectionBellFader_DefaultOn':'No'}
        user_settings.save_user_settings(reqargs)
        # when
        fadeInSettings = get_fade_in_settings_from_config()
        # then
        assert fadeInSettings == None
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()