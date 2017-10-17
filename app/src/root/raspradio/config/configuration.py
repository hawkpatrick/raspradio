'''
Created on 16.10.2017

@author: pho
'''
import configparser, os

config_holder = None
common_config_holder = None

def read_config_value(section, value):
    global config_holder
    if (config_holder == None):
        config_holder = init_config_holder()
    if (config_holder.has_option(section, value)):
        return config_holder.get(section, value)
    return get_config_from_common_config(section, value)
    
def get_config_from_common_config(section, value):
    global common_config_holder
    if (common_config_holder == None):
        common_config_holder = init_common_config_holder()
    return common_config_holder.get(section, value)

def init_common_config_holder():
    conf = configparser.ConfigParser()
    path = get_config_path()
    conf.read(path)
    return conf


def init_config_holder():
    conf = configparser.ConfigParser()
    path = get_common_config_path()
    conf.read(path)
    return conf

def get_config_path():
    base = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files')
    if is_env_raspberry():
        return base + "/raspberry.ini"
    else:
        return base + "/pho-lenox.ini"
    
def get_common_config_path():
    base = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files')
    return base + "/common.ini"    


def is_env_raspberry():
    return "raspberry" in read_hostname()


def read_hostname():
    with open('/etc/hostname', 'r') as f:
        return f.readline()