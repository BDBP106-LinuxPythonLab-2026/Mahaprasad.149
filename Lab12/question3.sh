#!/bin/bash

echo "Enter a number"
read number

n=1
until [ "$n" -gt 15 ]
do 
	echo "$(($n * $number))"
       n=$[$n+1]	
done
