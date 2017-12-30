from root.raspradio.config.configuration import get_user_config_path
import configparser
from root.raspradio.config import configuration

def save_user_settings(reqargs):
    configPath = get_user_config_path()
    config = configparser.ConfigParser()
    # This prevents that config-keys get toLowerCase automatically
    config.optionxform = str
    for key, value in reqargs.iteritems():
        splitted = key.split("_")
        if len(splitted) == 2:
            section = splitted[0]
            configKey = splitted[1]
            if not config.has_section(section):
                config.add_section(section)
            config.set(section, configKey, value)

    with open(configPath, 'w') as configfile:
        config.write(configfile)
    configuration.on_user_config_update()
    
def get_user_settings():
    return configuration.get_user_items_as_dict()


