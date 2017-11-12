'''
Created on 19.10.2017

@author: pho
'''
import os

def get_path_to_database_folder():
    current_path = os.path.abspath(os.path.dirname(__file__))
    current_path = os.path.join(current_path, os.pardir, os.pardir, 'resources', 'database')
    return current_path

def get_path_to_streams_file():
    current_path = get_path_to_database_folder()
    return current_path + "/streams_backup"

def get_path_to_alarms_file():
    current_path = get_path_to_database_folder()
    return current_path + "/alarms_backup"