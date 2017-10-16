'''
Created on 16.10.2017

@author: pho
'''
import configparser, os

config_holder = None

def read_value_http_server(value):
    global config_holder
    if (config_holder == None):
        config_holder = open_config_file()
    return config_holder.get("SectionHttpServer", value)

def open_config_file():
    conf = configparser.ConfigParser()
    path = get_config_path()
    conf.read(path)
    return conf

def get_config_path():
    base = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files')
    print "base: " + base
    if is_env_raspberry():
        return base + "/raspberry.ini"
    else:
        return base + "/pho-lenox.ini"


def is_env_raspberry():
    return "raspberry" in read_hostname()


def read_hostname():
    with open('/etc/hostname', 'r') as f:
        return f.readline()