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


OLD_IFS=$IFS
IFS=''

# file1_data=$( cat $1 )
# file2_data=$( cat $2 )


# file1_sub=''
flag=''
# touch /tmp/comp_tmp_file1.txt
myfile1=$(mktemp)
DONE=false
until $DONE ;do
    read -r line || DONE=true
    if [ -z $flag ]; then
        if echo "$line" | grep -Eq "string:"; then
            flag="true"
            # file1_sub="$(echo "$line" | grep -Eo "string:.*")"
            echo "$line" | grep -Eo "string:.*" > "$myfile1"
        fi
    else
        # file1_sub="${file1_sub}\n${line}"
        echo "$line" >> "$myfile1"
    fi
done < $1


if [ -z $flag ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! В первом файле не найдено подстроки \"string:\"
    fi
    IFS=$OLD_IFS
    exit 2
fi

# file2_sub=''
flag=''

# touch /tmp/comp_tmp_file2.txt
myfile2=$(mktemp)
DONE=false
until $DONE ;do
    read -r line || DONE=true
    if [ -z $flag ]; then
        if echo "$line" | grep -Eq "string:"; then
            flag="1"
            # file2_sub="$(echo "$line" | grep -Eo "string:.*")"
            echo "$line" | grep -Eo "string:.*" > "$myfile2"
        fi
    else
        # file2_sub="${file2_sub}\n${line}"
        echo "$line" >> "$myfile2"
    fi
done < $2

if [ -z $flag ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! Во втором файле не найдено подстроки \"string:\"
    fi
    IFS=$OLD_IFS
    exit 2
fi


# echo $file1_sub
# echo $file2_sub

IFS=$OLD_IFS


if cmp -s "$myfile1" "$myfile2"; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Файлы совпадают
    fi
    IFS=$OLD_IFS
    exit 0
else
    if echo "$3" | grep -Eq "^-v$"; then
        echo Файлы не совпадают
    fi
    IFS=$OLD_IFS
    exit 1
fi

# if [ "$file1_sub" == "$file2_sub" ]; then
#     if echo "$3" | grep -Eq "^-v$"; then
#         echo Файлы совпадают
#     fi
#     IFS=$OLD_IFS
#     exit 0
# else
#     if echo "$3" | grep -Eq "^-v$"; then
#         echo Файлы не совпадают
#     fi
#     IFS=$OLD_IFS
#     exit 1
# fi