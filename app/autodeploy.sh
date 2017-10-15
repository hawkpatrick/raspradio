lastdeploy=$(date -d "-1 years" +%s)
entrydate=$(date -d 2014-08-19 +%s)
RED='\033[0;31m'
NC='\033[0m' # No Color
GREEN='\033[0;32m'
fileschanged=false

while true; do

  fileschanged=false
  filesfound="$(find src -type f -not -name '*.swp')"
  for entry in $filesfound
  do
    entrydate=$(date -r "$entry" +%s)
    if [ $entrydate -ge $lastdeploy ];
    then
      fileschanged=true
    fi
  done
  if [ "$fileschanged" = true ]
  then
    scp -r src pi@192.168.0.220:/home/pi/app
    echo -e "${GREEN}Deployed http${NC} at "$(date)
  fi
  lastdeploy=$(date +%s)
  sleep 2
done
