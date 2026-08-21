#!/bin/bash

read -ra numbers < nums.txt
echo ${numbers[*]}

for i in ${numbers[*]}
do
	doublenum=$[i*2]
	echo "$doublenum"

done

