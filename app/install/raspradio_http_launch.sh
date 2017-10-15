#!/bin/bash
# raspradio_http_launcher.sh

sleep 10
cd /home/pi/app/src/root/raspradio
source flask/bin/activate
python radio.py
cd /
