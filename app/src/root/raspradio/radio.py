#!env/bin/python
'''
Created on 15.10.2017

@author: pho
'''
from flask import Flask, jsonify, make_response, request, render_template
import json

import threading
import os
import streams, control_vlc
import ring_alarm
from config import configuration

# Timezone muss gesetzt werden
os.environ['TZ'] = 'Europe/Paris'

alarms = []

app = Flask(__name__)

class Alarm: 
    def __init__(self, alarmid, hour, minute):
        self.alarmid = alarmid
        self.hour = hour
        self.minute = minute
        self.streamname = ''

    def __repr__(self):
        return self.toJSON()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def get_path_to_backup_file():
    return "files/alarms_backup"



def check_for_alarm():
    for alarm in alarms:
        ring_alarm.evaluate_alarm(alarm)
    threading.Timer(5.0, check_for_alarm).start()

def start_batch_thread():
    t1 = threading.Thread(target=check_for_alarm, args=[])
    t1.start()

def add_new_alarm(alarm):
    alarms.append(alarm)
    save_timers_to_file()


def delete_alarm(alarmid):
    index = -1
    for i, alarm in enumerate(alarms):
        if alarm.alarmid == alarmid:
            index = i
    if index > -1:
        del alarms[index]
    control_vlc.vlccmd('pl_stop')
    save_timers_to_file()
    return ""


def load_timers_from_file():
    if not os.path.isfile(get_path_to_backup_file()):
        return
    with open(get_path_to_backup_file(), "r") as timersfile:
        for line in timersfile:
            line = line.strip()
            alarmdict = json.loads(line)
            alarm = Alarm(alarmdict['alarmid'], alarmdict['hour'], alarmdict['minute'])
            alarms.append(alarm)

def save_timers_to_file():
    with open(get_path_to_backup_file(), 'w') as the_file:
        for alarm in alarms:
            alarmstr = alarm.toJSON()
            line = str(alarmstr).replace('\n', ' ').replace('\r', '')
            the_file.write(line + '\n')

@app.route('/alarm/app/v1.0/streams', methods=['GET'])
def http_get_configure_streams():
    return streams.http_configure_streams(request.args)

@app.route('/alarm/app/v1.0/alarm', methods=['GET'])
def alarm_main():
    reqargs = request.args
    if ('deleteme' in reqargs):
        delete_alarm(reqargs['deleteme'])
    if ('hour' in reqargs and 'minute' in reqargs):
        hour = reqargs['hour']
        minute = reqargs['minute']
        streamname = reqargs['stream']
        a = Alarm(str(len(alarms)), hour,minute)
        a.streamname = streamname
        add_new_alarm(a)
    return render_template('Start.html', aktivewecker=alarms[:], streams=streams.radio_streams[:])

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def get_host_from_config():
    return configuration.read_config_value("SectionHttpServer", "Url")

if __name__ == '__main__':  
    load_timers_from_file()
    streams.load_streams_from_file()
    start_batch_thread()
    app.run(debug=True,host=get_host_from_config(),port=8080, use_reloader=False)
    #app.run(debug=True,host='192.168.0.220',port=8080, use_reloader=False)








        

