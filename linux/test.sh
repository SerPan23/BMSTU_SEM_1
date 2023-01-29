#!/bin/bash

count=0
summ=0
max_num=-1
while read num; do
    if [[ "$num" =~ ^[0-9]+$ ]] ; then
        if [[ $num -eq 0 ]] ; then
            break
        fi
        count=$(($count + 1))
        summ="$summ+$num"
        if [[ $num -gt $max_num ]] ; then
            max_num=$num
        fi
    else
        exit 1
    fi
done

if [ $count -eq 0 ]; then
    exit 1
fi


res=$(echo "(${summ})/${count}" | bc)

echo $res
echo $max_num

exit