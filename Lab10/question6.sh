#!/bin/bash
echo "Input a number: "
read n

if [ "$n" -gt 100 ];then
	echo "The number is greater than 100."
else
	echo "The number is not greater than 100."
fi
if [ "$n" -gt 100 ];then
	echo "The number is greater than 100"
fi


# Corrected lines:
# Line 5: [[ changed to [ , ) changed to ] , no space between ; & then
# Line 10: [[ changed to [ , }] changed to ] , ; putted before then and no space

