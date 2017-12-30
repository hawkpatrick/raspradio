# state: {playing,paused}
# volume: {0-256}
from root.raspradio.vlc import control_vlc


def get_player_state():
    state = "playing" if control_vlc.vlc_is_playing() else "stopped"
    vlc_volume = control_vlc.vlc_read_volume()
    volume = _convert_volume_from_vlc(vlc_volume)
    return {"state": state, "volume": int(volume)}


def _convert_volume_from_vlc(vlc_volume):
    return float(vlc_volume) / float(256) * 100