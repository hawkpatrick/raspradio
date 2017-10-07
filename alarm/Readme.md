0. a) Flash raspian lite image on sd card (using etcher, see raspberry/tools/etcher...)
   b) Activate ssh by playcing an empty file called "ssh" into the boot folder
   c) After first login change password, change keyboard layout (/etc/config/keyboard

1. Copy install.sh to /home/pi/
2. Copy playlist.m3u to /home/pi/
3. "cd /home/pi"
4. "sudo ./install.sh /home/pi/playlist.m3u"
5. "exec bash" (or restart raspberry)
