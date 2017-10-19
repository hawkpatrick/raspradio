'''
Created on 15.10.2017

@author: pho
'''
import unittest
from mock import patch
from root.raspradio import ring_alarm, streams
from root.raspradio.alarms import Alarm
from mock import ANY

class RingAlarmTest(unittest.TestCase):


    def setUp(self):
        streams.radio_streams = []


    def tearDown(self):
        pass

    
    @patch('root.raspradio.ring_alarm.control_vlc')
    @patch('root.raspradio.streams.control_vlc')
    def test_ring_ring_calls_vlc_if_stream_found(self, mock_control_vlc, mock_control_vlc_2):
        """"Tests if vlc-play is called with the exact url when a matching stream was found"""
        streams.add_new_stream("Klassik Radio", "url")
        alarm = Alarm("1","00","00")
        alarm.streamname = "Klassik Radio"
        ring_alarm.ring_ring(alarm)
        mock_control_vlc.vlcplaystream.assert_called_with("url")
        
    @patch('root.raspradio.ring_alarm.control_vlc')
    @patch('root.raspradio.streams.control_vlc')
    def test_ring_ring_calls_vlc_if_stream_not_found(self, mock_control_vlc, mock_control_vlc_2):
        """"Tests if vlc-play is called with any command when no stream was found"""
        alarm = Alarm("1","00","00")
        alarm.streamname = "Klassik Radio"
        ring_alarm.ring_ring(alarm)
        mock_control_vlc_2.vlccmd.assert_called_with(ANY)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    