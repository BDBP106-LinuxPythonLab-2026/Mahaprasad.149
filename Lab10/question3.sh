#!/bin/bash

echo "Enter filename."
read file

if [ -f "$file" ];then
	echo "The file exists"
	exit 200
else
	exit 201
	echo "The file does not exists."
fi


echo 'outside the if-block'



