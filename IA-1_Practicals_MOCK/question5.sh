#!/bin/bash

arg1=$1
arg2=$2
arg3=$3
arg4=$4

if [ "$#" -ne 4 ]; then
	echo "Error: There are less than 4 arguments"
	exit 
else

echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Argument 3: $3"
echo "Argument 4: $4"

fi
