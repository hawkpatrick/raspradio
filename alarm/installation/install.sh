# $1 : The path to a playlist
#      The playlist must be placed at the raspberry, e.g. /home/pi/Desktop/playlist.m3u
#      or in the internet
if [ $# -lt 1 ]; then
  echo 1>&2 "$0: not enough arguments"
  echo "Parameter must be the path to a playlist file, e.g. /home/pi/Desktop/playlist.m3u"
  exit 2
fi 

# Install vlc player (as sudo)
echo "Installing vlc player..."
sudo apt-get update
sudo apt-get install vlc
echo "Finished installing vlc player"

# Kopieren der Datei initraspradiovlc... Dort steht drin, dass der VLC gestartet werden soll
# Die Datei wird zum Systemstart als Servie hinzugefügt
sudo cp /home/pi/initraspradiovlc /etc/init.d/initraspradiovlc
sudo chmod 755 /etc/init.d/initraspradiovlc
sudo update-rc.d /etc/init.d/initraspradiovlc defaults

# Install virtualenv (for python)
# TODO
