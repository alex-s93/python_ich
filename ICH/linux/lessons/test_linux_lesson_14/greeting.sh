#!/bin/bash

if [ $# -eq 0 ]
then
	 echo "You need take one argument: for exemple /path/to/file 'you data'"
exit 1
fi 
NAME=$1

echo "Greeting, $NAME!"
