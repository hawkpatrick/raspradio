
** Links 

basiert auf Tutorial: 
  https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
neuer Version des Tutorial: 
  https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
Flask API: 
  http://flask.pocoo.org/docs/0.12/api/


** Python-Komponenten: 


** Vorraussetzungen

* Installation von virtualenv nötig (siehe Tutorial bzw. Schritte unten)
* Installation von flask in der virtualenv nötig (siehe Tutorial bzw. Schritte unten)

Vorbereitung: 
  # installiere virtualenv (vermutlich nicht der beste Weg, sondern 
  # wie hier http://raspberry.io/wiki/how-to-get-python-on-your-raspberrypi/)
  $ sudo apt-get install virtualenv
  $ mdkir http
  $ cd http
  # installiere flask
  $ virtualenv flask
  $ flask/bin/pip install flask

* Eventuell müssen Libraries nachinstalliert werden, z.B. requests mit
  $ cd /home/pi/http
  $ flask/bin/pip install requests
  $ flask/bin/pip install python-dateutil
  $ flask/bin/pip install configparser
  $ flask/bin/pip install mock
  $ flask/bin/pip install flask-httpauth

* Flask aktivieren: 
  $ cd flask
  $ source bin/activate

* Das selbe für batch, bspw. im Ordner /home/pi/batch

  
*** Installation mit IntelliJ *** 

* git auschecken 
* intellij öffnen
* "import from existing sources" und zum ausgecheckten src ordner navigieren
* Projekt-Einstellungen öffnen (f4) -> "Platform Settings" -> "SDKs" -> "Packages" -> "+" -> die oben genannten Libraries installieren (requests, pyhton-dateutil, etc)

*** Deployment ***

* Der Python-Code liegt in der Datei 'httpserver.py', daneben gibt es noch HTML-Dateien und ein Start-Skript (raspradio_http_launch.sh) 
* mit dem Skript deploy.sh werden die relevanten Dateien auf dem Raspi kopiert (ggfs. anpasssen)
* Gestartet mit bspw.
    $ python httpserver.py
    oder
    $ ./httpserver.py

*** Code Erklärung ***

  * durch 'python httpserver.py' wird ein REST- bzw. HTTP-Server gestartet
  * Achtung: der Host ist aktuell hart kodiert auf 192.168.0.220 mit Port 8080 (siehe Zeile app.run)
  * ohne explizite Angabe des Hosts und Ports nicht von außen erreichbar!

* es fehlt noch das Thema Authentifzierung (falls nötig)


*** API COMMANDS ***

curl -i -H "Content-Type: application/json" -X POST -d '{"hour":20, "minute":10}' http://192.168.0.220:8080/alarm/api/v1.0/alarms

http://192.168.0.220:8080/alarm/app/v1.0/alarm


*** Installation als Startup-Kommando ***

scp initraspradiohttp pi@192.168.0.220:/home/pi/http
(auf dem PI)
sudo cp /home/pi/http/initraspradiohttp /etc/init.d
cd /etc/init.d
sudo chmod 755 initraspradiohttp
sudo update-rc.d initraspradiohttp defaults

Testen mit "/etc/init.d/initraspradiohttp start". 
Das selbe muss auch mit dem batch-Programm gemacht werden.


*** API COMMANDS ALT (TODO-API aus Tutorial -> anpassen!)

curl -i http://192.168.0.220:8080/todo/api/v1.0/tasks

curl -i http://localhost:5000/todo/api/v1.0/tasks/1

curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks

curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2

todo: delete gibt es natürlich auch...


