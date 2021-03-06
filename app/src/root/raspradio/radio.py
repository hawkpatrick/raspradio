#!env/bin/python

from flask import Flask, jsonify, make_response, request, render_template

import os
from root.raspradio import streams
from root.raspradio.alarms import watch_alarms
from root.raspradio.alarms import alarm
from root.raspradio.config import user_settings, configuration

# Timezone muss gesetzt werden
from root.raspradio.player import render_player, control_player
from root.raspradio.vlc import vlc_server

os.environ['TZ'] = 'Europe/Paris'

app = Flask(__name__)

list_alarms = "list_alarms"
new_alarm = "new_alarm"
configure_streams = "configure_streams"
configure_settings = "configure_settings"
player = "player"


html_links = {
    list_alarms: list_alarms,
    configure_streams: configure_streams,
    new_alarm : new_alarm,
    configure_settings : configure_settings,
    player : player
    }


@app.route('/raspradio/list_alarms', methods=['GET'])
def entrypoint_list_alarms():
    reqargs = request.args
    config = user_settings.get_user_settings()
    if ('deleteme' in reqargs):
        handle_request_delete_alarm(reqargs)
    if ('hour' in reqargs and 'minute' in reqargs):
        handle_request_new_alarm(reqargs)
    if 'new_alarm' in reqargs:
        return render_template(
            html_links[new_alarm] + ".html", 
            html_links = html_links,
            config = config,
            aktivewecker = alarm.all_alarms[:], 
            streams = streams.radio_streams[:])
    return render_template(
        html_links[list_alarms] + ".html", 
        html_links=html_links,
        aktivewecker=alarm.all_alarms[:], 
        streams=streams.radio_streams[:])
    
@app.route('/raspradio/configure_settings', methods=['GET'])
def entrypoint_configure_settings():
    reqargs = request.args
    streams.http_configure_streams(reqargs)
    if 'update_settings' in reqargs:
        user_settings.save_user_settings(reqargs)
    config = user_settings.get_user_settings()
    return render_template(
        html_links[configure_settings] + ".html", 
        html_links=html_links,
        streams=streams.radio_streams[:],
        config=config)     

@app.route('/raspradio/player', methods=['GET', 'POST'])
def entrypoint_player():
    reqargs = request.args
    control_player.on_input(reqargs)
    return render_template(
        html_links[player] + ".html",
        player_state=render_player.get_player_state(),
        html_links=html_links)

               
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def get_host_from_config():
    return configuration.read_config_value("SectionHttpServer", "Url")

def handle_request_new_alarm(reqargs):
    alarm.add_alarm_by_request_args(reqargs)

def handle_request_delete_alarm(reqargs):
    return alarm.delete_alarm(reqargs['deleteme'])


if __name__ == '__main__':  
    alarm.initialize()
    streams.load_streams_from_file()
    watch_alarms.start_watching()
    vlc_server.start_server()
    app.run(debug=True,host=get_host_from_config(),port=8080, use_reloader=False)
    #app.run(debug=True,host='192.168.0.220',port=8080, use_reloader=False)

        

