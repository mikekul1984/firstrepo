#!/bash/bin

fact=1

echo -e "enter a number"

read n

if [ $n -le 0 ]; then
 echo "invalid number"
 exit
fi
#factorial logic
if [ $n -gt 0 ]; then
 for ((i=$n;i>=1;i--))
 do
 fact='expr $fact \* $i'
 done
fi
echo "The factorial of $n is $fact"
