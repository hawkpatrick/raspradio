#!flask/bin/python
import threading
import datetime
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

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
    alarmtime = datetime.strptime(line, '%H:%M')
    now = datetime.now()
    if alarmtime.hour == now.hour and alarmtime.minute == now.minute:
        print "Alarm!!!!"
        vlcplay()
        

def printit():
    with open("timers", "r") as timersfile:
        i = 0
        for line in timersfile:
            i = i + 1
            line = line.strip()
            evaluateTimer(i, line)
    threading.Timer(5.0, printit).start()

  
printit()

