'''
Created on 19.10.2017

@author: pho
'''
from root.raspradio.database import db_access
import os, json
from root.raspradio.alarms import repeat_alarm
from root.raspradio.config import bell_config

all_alarms = []

def initialize():
    _load_alarms_from_file()
    
def add_alarm_by_request_args(reqargs):
    hour = reqargs['hour']
    minute = reqargs['minute']
    a = Alarm(str(len(all_alarms)), int(hour), int(minute))
    if 'stream' in reqargs:
        a.streamname = reqargs['stream']
    if 'fadein' in reqargs:
        a.isFadeInActive = True
    a.bellDurationSeconds = _get_bell_duration_in_seconds_from_reqargs(reqargs)
    if 'selectRepeatType' in reqargs:
        a.repeat = repeat_alarm.create_repetition(reqargs['selectRepeatType'], [])
    all_alarms.append(a)
    save_alarms_to_file()
    print "Added new alarm: " + str(a)


def _get_bell_duration_in_seconds_from_reqargs(reqargs):
    if not 'turnoff' in reqargs: 
        return 0
    if 'duration' in reqargs and reqargs['duration']:
        return int(reqargs['duration']) * 60
    return bell_config.get_stopper_duration_in_minutes() * 60


def delete_alarm(alarmid):
    index = -1
    for i, alarm in enumerate(all_alarms):
        if alarm.alarmid == alarmid:
            index = i
    if index > -1:
        del all_alarms[index]
    save_alarms_to_file()
    return ""

def save_alarms_to_file():
    pathToBackupFile = _get_path_to_alarms_backup_file()
    with open(pathToBackupFile, 'w') as the_file:
        for alarm in all_alarms:
            alarmstr = alarm.toJSON()
            line = str(alarmstr).replace('\n', ' ').replace('\r', '')
            the_file.write(line + '\n')
            
class Alarm: 
    
    def __init__(self, alarmid, hour, minute):
        self.alarmid = alarmid
        self.hour = hour
        self.minute = minute
        self.streamname = ''
        self.isActive = True
        self.isFadeInActive = False
        self.bellDurationSeconds = 30
        self.repeat = None

    def __repr__(self):
        return self.toJSON()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def _load_alarms_from_file():
    pathToBackupFile = _get_path_to_alarms_backup_file()
    if not os.path.isfile(pathToBackupFile):
        return
    with open(pathToBackupFile, "r") as timersfile:
        for line in timersfile:
            alarm = _create_alarm_from_string(line)
            all_alarms.append(alarm)
            
def _create_alarm_from_string(line):
    line = line.strip()
    alarmdict = json.loads(line)
    alarm = Alarm(alarmdict['alarmid'], alarmdict['hour'], alarmdict['minute'])
    alarm.streamname = alarmdict['streamname']
    if 'isFadeInActive' in alarmdict:
        alarm.isFadeInActive = alarmdict['isFadeInActive']
    if 'bellDurationSeconds' in alarmdict:
        alarm.bellDurationSeconds = alarmdict['bellDurationSeconds']
    if 'repeat' in alarmdict:
        alarm.repeat = repeat_alarm.create_repeat_from_dict(alarmdict['repeat'])
    return alarm


def _get_path_to_alarms_backup_file():
    return db_access.get_path_to_alarms_file()
