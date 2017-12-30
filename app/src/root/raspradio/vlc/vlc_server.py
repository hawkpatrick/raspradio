import os
import threading

from root.raspradio.vlc import control_vlc


def start_server():
    t1 = threading.Thread(target=_vlc_server_thread, args=[])
    t1.start()
    t2 = threading.Timer(5, _vlc_pause_player)
    t2.start()


def _vlc_server_thread():
    port = "43822"
    password = "hello"
    playlist = "/home/pi/playlist.m3u"
    bash_command = "vlc -I http --http-port %s --http-password %s %s" % (port, password, playlist)
    os.system("bash -c \"%s\"" % bash_command)


def _vlc_pause_player():
    control_vlc.vlc_pause()