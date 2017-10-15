#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for, render_template
import json
import requests
from datetime import datetime
from dateutil import parser
from requests.auth import HTTPBasicAuth
import threading
import os, time
from time import sleep
import urllib

# TZ muss gesetzt werden
os.environ['TZ'] = 'Europe/Paris'


alarms = []
streams = []

lastalarm = datetime.strptime('8/18/2008', "%m/%d/%Y")


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

class Stream:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return self.toJSON()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def find_stream_by_name(name):
    for stream in streams:
        if stream.name == name:
            return stream
    return None

def find_stream_index_by_name(name):
    for idx, stream in enumerate(streams):
        if stream.name == name:
            return idx
    return -1

def update_lastalarm(now):
    global lastalarm
    lastalarm = now

def must_evaluate_alarm(now):
    global lastalarm
    delta = now - lastalarm
    return delta.seconds > 60

def evaluate_alarm(alarm):
    now = datetime.now()
    if not must_evaluate_alarm(now):
        return
    line = "" + alarm.hour + ":" + alarm.minute
    alarmtime = parser.parse(line)
    if alarmtime.hour == now.hour and alarmtime.minute == now.minute:
        print "Alarm!!!!"
        if alarm.streamname:
            stream = find_stream_by_name(alarm.streamname)
            if stream:
                encodedstream = urllib.quote_plus(stream.url)
                vlcplaystream(encodedstream)
                update_lastalarm(now)
                return    
        vlccmd('pl_play')
        update_lastalarm(now)

def check_for_alarm():
    for alarm in alarms:
        evaluate_alarm(alarm)
    threading.Timer(5.0, check_for_alarm).start()

def start_batch_thread():
    t1 = threading.Thread(target=check_for_alarm, args=[])
    t1.start()

app = Flask(__name__)

def add_new_alarm(alarm):
    alarms.append(alarm)
    save_timers_to_file()

def add_new_stream(name, url):
    streams.append(Stream(name,url))
    save_streams_to_file()

def delete_stream(name):
    streamindex = find_stream_index_by_name(name)
    if streamindex < 0:
        return 
    del streams[streamindex]

@app.route('/alarm/app/v1.0/streams', methods=['GET'])
def http_get_configure_streams():
    reqargs = request.args
    if ('stream' in reqargs and 'name' in reqargs):
        stream = reqargs['stream']
        name = reqargs['name']
        if stream and name: 
            add_new_stream(name, stream)
    if 'deleteme' in reqargs:
        streamname = reqargs['deleteme']
        delete_stream(streamname)
    return render_template('Streams.html', streams=streams[:])

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
        print a
        add_new_alarm(a)
    return render_template('Start.html', aktivewecker=alarms[:], streams=streams[:])

def delete_alarm(alarmid):
    index = -1
    for i, alarm in enumerate(alarms):
        if alarm.alarmid == alarmid:
            index = i
    if index > -1:
        del alarms[index]
    vlccmd('pl_stop')
    save_timers_to_file()
    return ""


def load_timers_from_file():
    if not os.path.isfile("alarms_backup"):
        return
    with open("alarms_backup", "r") as timersfile:
        for line in timersfile:
            line = line.strip()
            alarmdict = json.loads(line)
            alarm = Alarm(alarmdict['alarmid'], alarmdict['hour'], alarmdict['minute'])
            alarms.append(alarm)

def save_timers_to_file():
    with open('alarms_backup', 'w') as the_file:
        for alarm in alarms:
            alarmstr = alarm.toJSON()
            line = str(alarmstr).replace('\n', ' ').replace('\r', '')
            the_file.write(line + '\n')

def load_streams_from_file():
    if not os.path.isfile("streams_backup"):
        return
    with open("streams_backup", "r") as the_file:
        for line in the_file:
            line = line.strip()
            thedict = json.loads(line)
            stream = Stream(thedict['name'], thedict['url'])
            streams.append(stream)

# TODO generalisieren mit save_timers....
def save_streams_to_file():
    with open('streams_backup', 'w') as the_file:
        for stream in streams:
            streamstr = stream.toJSON()
            line = str(streamstr).replace('\n', ' ').replace('\r', '')
            the_file.write(line + '\n')
#
# VLC 
# 

def vlccmd(cmd):
    username = ""
    password = "hello"
    url = 'http://127.0.0.1:43822/requests/status.xml?command='+cmd
    values = {'username': username, 'password': password }
    res = requests.get(url, auth=(username, password))
    print res

def vlccmd_input(cmd,inputparam):
    username = ""
    password = "hello"
    url = 'http://127.0.0.1:43822/requests/status.xml?command='+cmd+"&input="+inputparam
    values = {'username': username, 'password': password }
    res = requests.get(url, auth=(username, password))
    print res

def vlcplaystream(stream):
     vlccmd('pl_empty')
     vlccmd_input('in_enqueue', stream)
     vlccmd('pl_play')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':  
    load_timers_from_file()
    load_streams_from_file()
    start_batch_thread()
    app.run(debug=True,host='192.168.0.220',port=8080, use_reloader=False)








        

