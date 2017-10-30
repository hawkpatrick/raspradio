'''
Created on 15.10.2017

@author: pho
'''
import requests
from config import configuration
import xml.etree.ElementTree as ET


def get_vlc_host():
    return configuration.read_config_value("SectionVlcConnection", "VlcHost")


def get_vlc_port():
    return configuration.read_config_value("SectionVlcConnection", "VlcPort")

def vlccmd(cmd):
    url = vlc_get_base_url() + '/requests/status.xml?command=' + cmd
    vlccmd_by_url(url)

def vlc_get_base_url():
    return 'http://' + get_vlc_host() + ':' + get_vlc_port()

def vlccmd_input(cmd,inputparam):
    url = vlc_get_base_url() + '/requests/status.xml?command=' + cmd + "&input=" + inputparam
    vlccmd_by_url(url)
    
def vlccmd_by_url(url):
    username = ""
    password = "hello"
    res = requests.get(url, auth=(username, password))
    return res
    
def vlc_read_volume():
    document = vlc_read_status_as_document()
    vol = document.find('volume')
    result = int(vol.text)
    return result

def vlc_set_volume(volume):
    url = vlc_get_base_url() + '/requests/status.xml?command=volume&val=' + str(volume)
    vlccmd_by_url(url)

def vlc_increase_volume(delta):
    volume_now = vlc_read_volume()
    volume_after = delta + volume_now
    vlc_set_volume(volume_after)




def vlc_read_status_as_document():
    url = vlc_get_base_url() + '/requests/status.xml'
    content = vlccmd_by_url(url).content
    tree = ET.ElementTree(ET.fromstring(content))
    document = tree.getroot()
    return document



def vlc_play_stream(stream_url):
    vlccmd('pl_empty')
    vlccmd_input('in_enqueue', stream_url)
    vlccmd('pl_play')