import unittest
from root.raspradio.vlc import control_vlc
from mock import patch, call


class ControlVlcTest(unittest.TestCase):
    
    @patch('root.raspradio.vlc.control_vlc._vlc_cmd')
    @patch('root.raspradio.vlc.control_vlc._vlc_cmd_with_input')
    def testIncreaseVolume(self, mock_vlc_cmd_with_input, mock_vlc_cmd):
        # when
        control_vlc.vlc_play_stream('test')
        # then
        mock_vlc_cmd.assert_has_calls(calls=[call('pl_empty'), call('pl_play')])
        mock_vlc_cmd_with_input.assert_called_with('in_enqueue','test')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_upper']
    suite = unittest.TestLoader().loadTestsFromTestCase(ControlVlcTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 