#!flask/bin/python
import threading
import datetime
from datetime import datetime
from dateutil import parser
import requests
from requests.auth import HTTPBasicAuth
import os, time

lastalarm = None

def vlccmd(cmd):
    username = ""
    password = "hello"
    url = 'http://127.0.0.1:43822/requests/status.xml?command='+cmd
    values = {'username': username, 'password': password }
    res = requests.get(url, auth=(username, password))
    print res

def vlcplay():
    vlccmd('pl_play')

def evaluateTimer(linenumber, line):
    
    alarmtime = parser.parse(line)
    now = datetime.now()
    # print str(alarmtime) + ", now: " + str(now)
    if alarmtime.hour == now.hour and alarmtime.minute == now.minute:
        print "Alarm!!!!"
        lastalarm = datetime.now()
        vlcplay()
        

def printit():
    with open("timers", "r") as timersfile:
        i = 0
        for line in timersfile:
            i = i + 1
            line = line.strip()
            evaluateTimer(i, line)
    threading.Timer(5.0, printit).start()

# TZ muss gesetzt werden
os.environ['TZ'] = 'Europe/Paris'

printit()

