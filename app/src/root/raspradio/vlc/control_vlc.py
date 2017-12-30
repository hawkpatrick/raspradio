import requests
from root.raspradio.config import configuration
import xml.etree.ElementTree as ET


def vlc_set_volume(volume):
    url = _vlc_get_base_url() + '/requests/status.xml?command=volume&val=' + str(volume)
    _vlccmd_by_url(url)


def vlc_play_stream(stream_url):
    _vlc_cmd('pl_empty')
    _vlc_cmd_with_input('in_enqueue', stream_url)
    _vlc_cmd('pl_play')


def vlc_pause():
    _vlc_cmd('pl_pause')


def vlc_resume():
    _vlc_cmd('pl_play')


def vlc_is_playing():
    return 'playing' == _vlc_read_state()

def _vlc_get_host():
    return configuration.read_config_value("SectionVlcConnection", "VlcHost")


def _vlc_get_port():
    return configuration.read_config_value("SectionVlcConnection", "VlcPort")


def _vlc_get_base_url():
    return 'http://' + _vlc_get_host() + ':' + _vlc_get_port()


def _vlc_cmd(cmd):
    url = _vlc_get_base_url() + '/requests/status.xml?command=' + cmd
    _vlccmd_by_url(url)


def _vlc_cmd_with_input(cmd, inputparam):
    url = _vlc_get_base_url() + '/requests/status.xml?command=' + cmd + "&input=" + inputparam
    _vlccmd_by_url(url)


def _vlccmd_by_url(url):
    username = ""
    password = "hello"
    res = requests.get(url, auth=(username, password))
    return res


def vlc_read_volume():
    document = _vlc_read_status_as_document()
    vol = document.find('volume')
    result = int(vol.text)
    return result


def _vlc_read_state():
    document = _vlc_read_status_as_document()
    return document.find('state').text


def _vlc_read_status_as_document():
    url = _vlc_get_base_url() + '/requests/status.xml'
    content = _vlccmd_by_url(url).content
    tree = ET.ElementTree(ET.fromstring(content))
    document = tree.getroot()
    return document