#!/bin/bash

echo "Please provide your name!"
read USER_NAME
if [[ $USER_NAME == "" ]]
then
	echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR You should enter your name! " >> ./eroors.log
else
  echo "Greeting, $USER_NAME"
  date "+%d-%m-%Y"
  date "+%H:%M:%S"
  ps aux | grep -v "ps aux" | grep -v "grep" | wc -l
  cat /etc/os-release
fi
