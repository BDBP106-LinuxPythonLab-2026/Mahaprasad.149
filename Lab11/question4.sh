#!/bin/bash

val1=Jayashree
val2=Nagesh
if [ $val1 > $val2 ]; then
	echo "$val1 is greater than $val2"
else
	echo "$val1 is lesser than $val2"
fi

val1=Jayashree
val2=Nagesh

if [ $val1 \> $val2 ];then
	echo "$val1 is greater than $val2"
else
	echo "$val1 is lesser than $val2"
fi

 #This time the > symbol will not be interpreted as the redirection function; as the "\"b before it takes bash to ignore it.
