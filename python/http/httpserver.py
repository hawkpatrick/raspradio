#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for, render_template
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

def save_alarm(hour, minute):
    alarmstr = "" + str(hour) + ":" + str(minute)
    with open('../batch/timers', 'w') as the_file:
        the_file.write(alarmstr + '\n')
    return "Saved " + alarmstr

def get_active_alarms():
    lines = [line.rstrip('\n') for line in open('../batch/timers', 'r')]
    return lines

@app.route('/alarm/app/v1.0/alarm', methods=['GET'])
def alarm_main():
    print "Received request: " + str(request)
    reqargs = request.args
    if ('deleteme' in reqargs):
        delete_alarm()
    if ('hour' in reqargs and 'minute' in reqargs):
	hour = reqargs['hour']
	minute = reqargs['minute']
        save_alarm(hour,minute)
    weckers=get_active_alarms()
    print weckers
    return render_template('Start.html', aktivewecker=weckers)

def delete_alarm():
    open('../batch/timers', 'w').close()
    vlccmd('pl_stop')
    return ""


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

#
# TUTORIAL REST Interface
#


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Chees',
        'done': False
    }
]


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/alarm/app/v1.0/start', methods=['POST'])
def receive_new_alarm():
    print "Received request: " + request
    return ""

@app.route('/alarm/api/v1.0/alarms', methods=['POST'])
def create_alarm():
    hour = request.json['time']
    minute = request.json['minute']
    alarmstr = "" + str(hour) + ":" + str(minute)
    save_alarm(hour,minute)
    return jsonify({'alarm': alarmstr}), 201

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'tasks': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.220',port=8080)

