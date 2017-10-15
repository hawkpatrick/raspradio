'''
Created on 15.10.2017

@author: pho
'''
import requests

def vlccmd(cmd):
    url = 'http://127.0.0.1:43822/requests/status.xml?command=' + cmd
    vlccmd_by_url(url)

def vlccmd_input(cmd,inputparam):
    url = 'http://127.0.0.1:43822/requests/status.xml?command=' + cmd + "&input=" + inputparam
    vlccmd_by_url(url)
    
def vlccmd_by_url(url):
    username = ""
    password = "hello"
    res = requests.get(url, auth=(username, password))
    print res  

def vlcplaystream(stream):
    vlccmd('pl_empty')
    vlccmd_input('in_enqueue', stream)
    vlccmd('pl_play')