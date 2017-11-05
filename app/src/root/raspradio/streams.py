'''
Created on 15.10.2017

@author: pho
'''
from flask import render_template
import os, json, urllib, control_vlc
from database import db_access

radio_streams = []

class Stream:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return self.toJSON()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def get_path_to_backup_file():
    return db_access.get_path_to_streams_file()

def add_new_stream(name, url):
    radio_streams.append(Stream(name,url))
    save_streams_to_file()
    
    
def load_streams_from_file():
    if not os.path.isfile(get_path_to_backup_file()):
        print "Streams backup file not found!"
        return
    with open(get_path_to_backup_file(), "r") as the_file:
        for line in the_file:
            line = line.strip()
            thedict = json.loads(line)
            stream = Stream(thedict['name'], thedict['url'])
            radio_streams.append(stream)

def save_streams_to_file():
    with open(get_path_to_backup_file(), 'w') as the_file:
        for stream in radio_streams:
            streamstr = stream.toJSON()
            line = str(streamstr).replace('\n', ' ').replace('\r', '')
            the_file.write(line + '\n')

def http_configure_streams(reqargs):
    if ('stream' in reqargs and 'name' in reqargs):
        stream = reqargs['stream']
        name = reqargs['name']
        if stream and name: 
            add_new_stream(name, stream)
    if 'deleteme' in reqargs:
        streamname = reqargs['deleteme']
        delete_stream(streamname)
    return render_template('Streams.html', streams=radio_streams[:])

def find_stream_by_name(name):
    for stream in radio_streams:
        if stream.name == name:
            return stream
    return None

def find_stream_index_by_name(name):
    for idx, stream in enumerate(radio_streams):
        if stream.name == name:
            return idx
    return -1


def delete_stream(name):
    streamindex = find_stream_index_by_name(name)
    if streamindex < 0:
        return 
    del radio_streams[streamindex]
    
def play_stream(stream):
    encodedstream = urllib.quote_plus(stream.url)
    control_vlc.vlc_play_stream(encodedstream)


