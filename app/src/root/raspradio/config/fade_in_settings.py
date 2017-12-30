from root.raspradio.config.user_settings import get_user_settings


class FadeInSettings:
    
    def __init__(self, durationInSeconds):
        self.durationInSeconds = durationInSeconds


def get_fade_in_settings_from_config():
    userSettings = get_user_settings()
    defaultOn = userSettings['SectionBellFader']['DefaultOn']
    if not defaultOn or defaultOn == 'No':
        return None
    timespanInSeconds = userSettings['SectionBellFader']['TimespanInSeconds']
    return FadeInSettings(int(timespanInSeconds))
