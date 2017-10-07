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

# Writing file bash_aliases
# bash_aliases will be called automatically by bashrc 
# (bashrc is called at every startup, after login of the user)
# Calling bash_aliases will then call bash_alias_vlc
echo "Writing file bash_aliases"
echo "if [ -f ~/.bash_alias_vlc ]; then" >> /home/pi/.bash_aliases
echo "    . ~/.bash_alias_vlc" >> /home/pi/.bash_aliases
echo "fi" >> /home/pi/.bash_aliases
sudo chmod 777 /home/pi/.bash_aliases

# Writing file bash_alias_vlc
# Calling bash_alias_vlc will then start the vlc player streaming the playlist given in parameter $1
echo "Writing file bash_alias_vlc"
echo "echo 'Starting vlc server...'" >> /home/pi/.bash_alias_vlc
echo "cvlc -I http --http-port 43822 --http-password hello $1 > /dev/null" >> /home/pi/.bash_alias_vlc 
sudo chmod 777 /home/pi/.bash_alias_vlc

# Install virtualenv (for python)

