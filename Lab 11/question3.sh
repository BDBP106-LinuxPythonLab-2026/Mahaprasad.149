#!/bin/bash

echo "Give a string"
read string

if [ -n "$string" ];then
	echo "The string is not empty"
else
	echo "The string is empty"
fi

