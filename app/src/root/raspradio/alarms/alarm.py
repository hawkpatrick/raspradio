from root.raspradio.database import db_access
import os, json
from root.raspradio.alarms import repeat_alarm

all_alarms = []

def initialize():
    _load_alarms_from_file()
    
def add_alarm_by_request_args(reqargs):
    hour = reqargs['hour']
    minute = reqargs['minute']
    a = Alarm(str(len(all_alarms)), int(hour), int(minute))
    a.repetition = repeat_alarm.create_repetition(reqargs)
    all_alarms.append(a)
    save_alarms_to_file()
    print "Added new alarm: " + str(a)


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
        self.repetition = None
        self.isActive = True
        self.streamSetting = None
        self.fadeInSetting = None
        self.stopTheBellSettings = None

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
    alarm.streamSetting = alarmdict['streamSetting']
    if 'fadeInSetting' in alarmdict:
        alarm.fadeInSetting = alarmdict['fadeInSetting']
    if 'stopTheBellSettings' in alarmdict:
        alarm.stopTheBellSettings = alarmdict['stopTheBellSettings']
    if 'repetition' in alarmdict:
        alarm.repetition = repeat_alarm.create_repeat_from_dict(alarmdict['repetition'])
    return alarm


def _get_path_to_alarms_backup_file():
    return db_access.get_path_to_alarms_file()
