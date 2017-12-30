import configparser, os

config_holder = None
common_config_holder = None
user_config_holder = None

def read_config_value(section, value):
    global config_holder
    init_user_config_if_none()
    if (user_config_holder.has_option(section, value)):
        return user_config_holder.get(section, value)
    if (config_holder == None):
        config_holder = _init_config_holder()
    if (config_holder.has_option(section, value)):
        return config_holder.get(section, value)
    return _get_config_from_common_config(section, value)

def init_user_config_if_none():
    global user_config_holder
    if (user_config_holder == None): 
        user_config_holder = _init_user_config_holder()

def read_config_value_as_int(section, value):
    asString = read_config_value(section, value)
    return int(asString)

def on_user_config_update():
    global user_config_holder
    user_config_holder = _init_user_config_holder()

def get_user_config_path():
    base = _get_config_base_path()
    return base + "/user.ini" 

def get_user_items_as_dict():
    init_user_config_if_none()
    result = {}
    for section in user_config_holder.sections():
        result[section] = dict(user_config_holder.items(section))
    return result

def _get_config_from_common_config(section, value):
    global common_config_holder
    if (common_config_holder == None):
        common_config_holder = _init_common_config_holder()
    return common_config_holder.get(section, value)

def _init_common_config_holder():
    conf = configparser.ConfigParser()
    conf.optionxform = str
    path = _get_config_path()
    conf.read(path)
    return conf

def _init_user_config_holder():
    conf = configparser.ConfigParser()
    conf.optionxform = str
    path = get_user_config_path()
    conf.read(path)
    return conf

def _init_config_holder():
    conf = configparser.ConfigParser()
    conf.optionxform = str
    path = _get_common_config_path()
    conf.read(path)
    return conf

def _get_config_base_path():
    current_path = os.path.abspath(os.path.dirname(__file__))
    current_path = os.path.join(current_path, os.pardir, os.pardir, 'resources', 'config')
    return current_path

def _get_config_path():
    base = _get_config_base_path()
    if is_env_raspberry():
        return base + "/raspberry.ini"
    else:
        return base + "/pho-lenox.ini"
    
def _get_common_config_path():
    base = _get_config_base_path()
    return base + "/common.ini"    
 

def is_env_raspberry():
    return "raspberry" in _read_hostname()


def _read_hostname():
    with open('/etc/hostname', 'r') as f:
        return f.readline()