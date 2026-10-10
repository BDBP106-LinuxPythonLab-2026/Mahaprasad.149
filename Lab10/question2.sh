#!/bin/bash

echo "Enter filename."
read file

if [ -f "$file" ];then
	if [ -x "$file" ];then
		echo "The file exists and executable"
	else 
		echo "The file exists and not executable"
	fi
else
	echo "The file does not exists."
fi



