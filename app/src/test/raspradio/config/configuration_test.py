'''
Created on 16.10.2017

@author: pho
'''
import unittest
from mock import patch
from root.raspradio.config import configuration


class ConfigurationTest(unittest.TestCase):
    
    def setUp(self):
        configuration.common_config_holder = None
        configuration.config_holder = None

    @patch('root.raspradio.config.configuration.read_hostname')
    def test_is_env_raspberry(self, mock_read_hostname):
        mock_read_hostname.return_value = "raspberrypi"
        isRaspi = configuration.is_env_raspberry()
        assert isRaspi
    
    @patch('root.raspradio.config.configuration.is_env_raspberry')
    def test_read_a_config_value(self, mock_is_env_raspberry):
        """Reads the value SectionHttpServer#Url from the config. is_env_raspberry is mocked"""
        mock_is_env_raspberry.return_value = False
        actual_value = configuration.read_config_value("SectionHttpServer", "Url")
        assert actual_value == "127.0.0.1"
    
    @patch('root.raspradio.config.configuration.is_env_raspberry')
    def test_read_a_config_value_when_on_raspi(self, mock_is_env_raspberry):
        """Reads the value SectionHttpServer#Url from the config. is_env_raspberry is mocked"""
        mock_is_env_raspberry.return_value = True
        actual_value = configuration.read_config_value("SectionHttpServer", "Url")
        assert actual_value == "192.168.0.220"
        
    @patch('root.raspradio.config.configuration.is_env_raspberry')
    def test_read_a_config_from_common_config_file(self, mock_is_env_raspberry):
        mock_is_env_raspberry.return_value = False
        actual_value = configuration.read_config_value("SectionCommonTest", "AKey")
        assert actual_value == "AValue"
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()