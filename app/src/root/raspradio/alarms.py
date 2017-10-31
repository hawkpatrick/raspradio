'''
Created on 19.10.2017

@author: pho
'''
from database import db_access
import os, json

all_alarms = []

class Alarm: 
    def __init__(self, alarmid, hour, minute):
        self.alarmid = alarmid
        self.hour = hour
        self.minute = minute
        self.streamname = ''
        self.fadein = False
        self.duration = 30

    def __repr__(self):
        return self.toJSON()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def add_new_alarm(hour, minute, streamname, fadein, duration):
    a = Alarm(str(len(all_alarms)), hour, minute)
    a.streamname = streamname
    a.fadein = fadein
    a.duration = duration
    all_alarms.append(a)
    save_alarms_to_file()

def delete_alarm(alarmid):
    index = -1
    for i, alarm in enumerate(all_alarms):
        if alarm.alarmid == alarmid:
            index = i
    if index > -1:
        del all_alarms[index]
    save_alarms_to_file()
    return ""

def load_alarms_from_file():
    if not os.path.isfile(get_path_to_backup_file()):
        return
    with open(get_path_to_backup_file(), "r") as timersfile:
        for line in timersfile:
            line = line.strip()
            alarmdict = json.loads(line)
            alarm = Alarm(alarmdict['alarmid'], alarmdict['hour'], alarmdict['minute'])
            alarm.streamname = alarmdict['streamname']
            if 'fadein' in alarmdict:
                alarm.fadein = alarmdict['fadein']
            if 'duration' in alarmdict:
                alarm.duration = alarmdict['duration']
            all_alarms.append(alarm)

def save_alarms_to_file():
    with open(get_path_to_backup_file(), 'w') as the_file:
        for alarm in all_alarms:
            alarmstr = alarm.toJSON()
            line = str(alarmstr).replace('\n', ' ').replace('\r', '')
            the_file.write(line + '\n')



def get_path_to_backup_file():
    return db_access.get_path_to_alarms_file()
