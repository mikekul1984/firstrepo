#!/bin/bash

fact() {
	local num=$1
	if [ $num -eq 0 ]; then
		ret=1
	else
		temp=$((num-1))
		fact $temp
		ret=$((num*$?))
	fi
	return $ret
}

fact 5

echo "Factorial of 5 = $?"

exit 0
