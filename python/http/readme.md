
** Links 

basiert auf Tutorial: 
  https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
neuer Version des Tutorial: 
  https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
Flask API: 
  http://flask.pocoo.org/docs/0.12/api/

** Vorraussetzungen

* Installation von virtualenv nötig (siehe Tutorial bzw. Schritte unten)
* Installation von flask in der virtualenv nötig (siehe Tutorial bzw. Schritte unten)

Vorbereitung: 
  # installiere virtualenv (vermutlich nicht der beste Weg, sondern 
  # wie hier http://raspberry.io/wiki/how-to-get-python-on-your-raspberrypi/)
  $ sudo apt-get install virtualenv
  $ mdkir raspradiohttp
  $ cd raspradiohttp
  # installiere flask
  $ virtualenv flask
  $ flask/bin/pip install flask
  

** Deployment

* Code liegt in Datei 'app.py'
* nach Bearbeiten der Datei 'app.py' erfolgt das Kopieren: 
    $ scp /home/pho/raspberry/python/app.py pi@192.168.0.220:/home/pi/raspradiohttp
* Starten mit
    $ python app.py

* Code Erklärung: 
  * durch 'python app.py' wird ein REST-Server gestartet
  * der Host ist aktuell hart kodiert auf 192.168.0.220 mit Port 8080 (siehe Zeile app.run)
  * ohne explizite Angabe des Hosts und Ports nicht von außen erreichbar!

* es fehlt noch das Thema Authentifzierung (falls nötig)


*** API COMMANDS (TODO-API aus Tutorial -> anpassen!)

curl -i http://192.168.0.220:8080/todo/api/v1.0/tasks

curl -i http://localhost:5000/todo/api/v1.0/tasks/1

curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks

curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2

todo: delete gibt es natürlich auch...


curl -i -H "Content-Type: application/json" -X POST -d '{"hour":20, "minute":10}' http://192.168.0.220:8080/alarm/api/v1.0/alarms

http://192.168.0.220:8080/alarm/app/v1.0
