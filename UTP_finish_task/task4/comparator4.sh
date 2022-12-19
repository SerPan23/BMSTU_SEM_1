#!/bin/bash


if [ ! -f $1 ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! Файл 1 не найден!
    fi
    exit 2
fi
if [ ! -f $2 ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! Файл 2 не найден!
    fi
    exit 2
fi


if [ ! -r "$1" ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! У вас нет прав доступа к файлу 1!
    fi
    exit 2
fi
if [ ! -r "$2" ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! У вас нет прав доступа к файлу 2!
    fi
    exit 2
fi


# file1_data=$( cat $1 )
# file2_data=$( cat $2 )


# file1_nums=''
# for word in $file1_data; do
#     if [[ "$word" =~ ^[+-]?[0-9]+(\.[0-9]+)?(e[+-]?[0-9]+)?$ ]]; then
#         file1_nums="$file1_nums $word"
#     fi
# done

flag=''

myfile1=$(mktemp)
DONE=false
until $DONE ;do
    read -r line || DONE=true
    for word in $line; do 
        if [[ "$word" =~ ^[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?$ ]]; then
            flag='1'
            echo "$word" >> "$myfile1"
        fi
    done
done < $1



if [ -z $flag ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! В файле 1 нет ЧПТ
    fi
    exit 2
fi


# file2_nums=''
# for word in $file2_data; do
#     if [[ "$word" =~ ^[+-]?[0-9]+(\.[0-9]+)?(e[+-]?[0-9]+)?$ ]]; then
#         file2_nums="$file2_nums $word"
#     fi
# done



flag=''

myfile2=$(mktemp)
DONE=false
until $DONE ;do
    read -r line || DONE=true
    for word in $line; do 
        if [[ "$word" =~ ^[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?$ ]]; then
            flag='1'
            echo "$word" >> "$myfile2"
        fi
    done
done < $2

if [ -z $flag ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! В файле 2 нет ЧПТ
    fi
    exit 2
fi


# echo $file1_nums
# echo $file2_nums



if cmp -s "$myfile1" "$myfile2"; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Файлы совпадают
    fi
    exit 0
else
    if echo "$3" | grep -Eq "^-v$"; then
        echo Файлы не совпадают
    fi
    exit 1
fi



# if [ "$file1_nums" == "$file2_nums" ]; then
#     if echo "$3" | grep -Eq "^-v$"; then
#         echo Файлы совпадают
#     fi
#     exit 0
# else
#     if echo "$3" | grep -Eq "^-v$"; then
#         echo Файлы не совпадают
#     fi
#     exit 1
# fi