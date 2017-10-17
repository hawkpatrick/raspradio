'''
Created on 16.10.2017

@author: pho
'''
import unittest
from mock import patch
from root.raspradio.config import configuration


class ConfigurationTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    @patch('root.raspradio.config.configuration.read_hostname')
    def test_is_env_raspberry(self, mock_read_hostname):
        mock_read_hostname.return_value = "raspberrypi"
        isRaspi = configuration.is_env_raspberry()
        assert isRaspi
    
    @patch('root.raspradio.config.configuration.get_config_path')
    def test_read_a_config_value(self, mock_get_config_path):
        """Reads the value SectionHttpServer#Url from the config. get_config_path is mocked"""
        mock_get_config_path.return_value = "/home/pho/workspace/eclipse/python/raspradio/app/src/root/raspradio/config/files/pho-lenox.ini"
        assert configuration.read_config_value("SectionHttpServer", "Url") == "127.0.0.1"
    
    def test_get_config_path(self):
        assert "raspradio/config/files" in configuration.get_config_path()
  
    @patch('root.raspradio.config.configuration.get_config_path')
    def test_read_a_config_from_common_config_file(self, mock_get_config_path):
        mock_get_config_path.return_value = "/home/pho/workspace/eclipse/python/raspradio/app/src/root/raspradio/config/files/pho-lenox.ini"
        assert configuration.read_config_value("SectionCommonTest", "AKey") == "AValue"
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()