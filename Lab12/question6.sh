#!/bin/bash
function maximum {
	var1=$1
	var2=$2
	if [ $var1 -gt $var2 ];then
		echo "$var1 is greater"
	else
		echo "$var2 is greater"
	fi
}

result=$(maximum $1 $2)
echo $result
