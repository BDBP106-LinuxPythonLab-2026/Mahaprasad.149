#!/bin/bash

echo "Enter filename:"
read file

#Check if anything (file/directory/symlink/etc) exists
if [ -e $file ];then
	echo "$file exists"
else
	echo "$file doesnot exist"
fi

#check if the file exits and is not empty.

if [ -s $file ];then
	echo "The file exists and has data"
else
	echo "The file is either empty or doesnot exist"
fi

#check if the files is there or not.

if [ -f $file ];then
	echo "The file exists"
else
	echo "The file does not exist"
fi


