'''
Created on 15.10.2017

@author: pho
'''
import unittest
from root.raspradio import streams
from root.raspradio.streams import Stream
from mock import patch


class StreamsTest(unittest.TestCase):


    def setUp(self):
        streams.radio_streams = []


    def tearDown(self):
        streams.radio_streams = []
        streams.save_streams_to_file()


    def test_add_stream(self):
        streams.add_new_stream("Klassik Radio", "www.klassik.de") 
        assert len(streams.radio_streams) is 1 
        
    def test_stream_backup_save_and_load(self):  
        streams.add_new_stream("Klassik Radio", "www.klasik.de")
        streams.add_new_stream("Pop Radio", "www.pop.de")
        streams.radio_streams = []
        streams.load_streams_from_file()
        assert len(streams.radio_streams) == 2
        assert streams.radio_streams[0].name == "Klassik Radio"
        assert streams.radio_streams[1].url == "www.pop.de"
        
    @patch('root.raspradio.streams.render_template')
    def test_html_request_adds_stream(self, mock_render_template):
        req = {'name': 'Test Radio', 'stream': 'http://www.klassikradio.de/'}
        streams.http_configure_streams(req)
        assert len(streams.radio_streams) is 1
        assert streams.radio_streams[0].name == 'Test Radio'
        
    @patch('root.raspradio.streams.render_template')
    def test_html_request_deletes_stream(self, mock_render_template):
        streams.radio_streams = [Stream("Deleteable Radio", "www.delete.de")]
        req = {'deleteme': 'Deleteable Radio'}
        streams.http_configure_streams(req)
        assert len(streams.radio_streams) is 0



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(StreamsTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 
    
    
