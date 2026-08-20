#!/bin/bash

#(i)

var1=Testing
var2=testing

#(ii)

if [ $var1 \> $var2 ];then
	echo "$var1 is greater than $var2"
else
	echo "$var1 is lesser than $var2"
fi

#(iii)
# Testing is lesser than testing.

#(iv)

echo "$var1" > Teststringfile
echo "$var2" >> Teststringfile

#(v)

sort Teststringfile
#Testing is greater than testing.
#The result of sort is opposite from if. The sort treats the uppercase as greater than lowercase, whereas, the if treats the lowercase as greaterthan the uppercase by default.
