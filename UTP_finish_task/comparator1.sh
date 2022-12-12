#!/bin/bash

file1_data=$( cat $1)
file2_data=$( cat $2)

file1_nums=''
for word in $file1_data; do
    # echo $word
    if [[ "$word" =~ ^[-+]?[0-9]+$ ]]; then
        file1_nums="$file1_nums $word"
        # echo $file1_nums
    fi
done

file2_nums=''
for word in $file2_data; do
    if [[ "$word" =~ ^[-+]?[0-9]+$ ]]; then
        file2_nums="$file2_nums $word"
    fi
done

if [ "$file1_nums" == "$file2_nums" ]; then
    exit 0
else
    exit 1
fi