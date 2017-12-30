from root.raspradio.bells import bell
from root.raspradio.vlc import control_vlc


def _convert_volume_to_vlc(volumeInPercent):
    volume = float(volumeInPercent) / float(100) * 256
    return int(volume)


def on_input(reqargs):
    if not 'play_control' in reqargs:
        return
    control_action = _get_control_button_value(reqargs)
    if control_action is not None:
        bell.remove_player_control_from_current_bell()
    if control_action == 'Play':
        control_vlc.vlc_resume()
    if control_action == 'Stop':
        control_vlc.vlc_pause()
    newVolume = _get_volume_slider_value(reqargs)
    if newVolume is not None:
        bell.remove_volume_control_from_current_bell()
        control_vlc.vlc_set_volume(_convert_volume_to_vlc(newVolume))


def _get_control_button_value(reqargs):
    if 'play_control_value' in reqargs:
        return reqargs['play_control_value']
    return None

def _get_volume_slider_value(reqargs):
    if 'volumeSlider' in reqargs:
        return reqargs['volumeSlider']
    return None