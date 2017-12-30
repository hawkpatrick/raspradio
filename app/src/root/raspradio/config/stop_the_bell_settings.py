from root.raspradio.config.user_settings import get_user_settings

class StopTheBellSettings:
    
    def __init__(self, turnOffAfterMinutes):
        self.turnOffAfterMinutes = turnOffAfterMinutes

def get_stop_the_bell_settings_from_config():
    userSettings = get_user_settings()
    defaultOn = userSettings['SectionBellStopper']['DefaultOn']
    if not defaultOn or defaultOn == 'No':
        return None
    turnOffAfterMinutes = userSettings['SectionBellStopper']['DurationInMinutes']
    return StopTheBellSettings(int(turnOffAfterMinutes))