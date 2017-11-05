#!env/bin/python
'''
Created on 15.10.2017

@author: pho
'''
from flask import Flask, jsonify, make_response, request, render_template

import os
from root.raspradio import streams, alarms, watch_alarms
from config import configuration

# Timezone muss gesetzt werden
os.environ['TZ'] = 'Europe/Paris'

app = Flask(__name__)

@app.route('/alarm/app/v1.0/streams', methods=['GET'])
def http_get_configure_streams():
    return streams.http_configure_streams(request.args)

@app.route('/alarm/app/v1.0/alarm', methods=['GET'])
def alarm_main():
    reqargs = request.args
    if ('deleteme' in reqargs):
        handle_request_delete_alarm(reqargs)
    if ('hour' in reqargs and 'minute' in reqargs):
        handle_request_new_alarm(reqargs)
    return render_template('Start.html', aktivewecker=alarms.all_alarms[:], streams=streams.radio_streams[:])

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def get_host_from_config():
    return configuration.read_config_value("SectionHttpServer", "Url")

def handle_request_new_alarm(reqargs):
    alarms.add_alarm_by_request_args(reqargs)

def handle_request_delete_alarm(reqargs):
    return alarms.delete_alarm(reqargs['deleteme'])


if __name__ == '__main__':  
    alarms.load_alarms_from_file()
    streams.load_streams_from_file()
    watch_alarms.start_watching()
    app.run(debug=True,host=get_host_from_config(),port=8080, use_reloader=False)
    #app.run(debug=True,host='192.168.0.220',port=8080, use_reloader=False)








        

