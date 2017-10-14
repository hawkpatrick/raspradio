lastdeploy=$(date -d "-1 years" +%s)
entrydate=$(date -d 2014-08-19 +%s)
RED='\033[0;31m'
NC='\033[0m' # No Color
GREEN='\033[0;32m'
httpchanged=false
batchchanged=false

while true; do

  batchchanged=false
  filesinbatch="$(find batch -type f -not -name '*.swp')"
  for entry in $filesinbatch
  do
    entrydate=$(date -r "$entry" +%s)
    if [ $entrydate -ge $lastdeploy ];
    then 
      batchchanged=true
    fi
  done

  httpchanged=false
  filesinhttp="$(find http -type f -not -name '*.swp')"
  for entry in $filesinhttp
  do
    entrydate=$(date -r "$entry" +%s)
    if [ $entrydate -ge $lastdeploy ];
    then
      httpchanged=true
    fi
  done
  if [ "$httpchanged" = true ]
  then
    scp -r http pi@192.168.0.220:/home/pi
    echo -e "${GREEN}Deployed http${NC} at "$(date)
  fi
  if [ "$batchchanged" = true ]
  then
    scp -r batch pi@192.168.0.220:/home/pi
    echo -e "${GREEN}Deployed batch${NC} at "$(date)
  fi
  lastdeploy=$(date +%s)
  sleep 5
done
