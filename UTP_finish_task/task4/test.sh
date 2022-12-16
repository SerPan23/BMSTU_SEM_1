#!/bin/bash

separator='---------------------------------------'

echo Тестирование скрипта вариант 4
echo Все тесты будут запущенны с флагом -v
echo После каждого теста будет выводиться полученный код возврата
echo



echo "$separator"
echo Тест 1: файлы совпадают
bash ./comparator4.sh "./tests/file1.txt" "./tests/file1.txt" -v
echo Код возврата: "$?"
echo "$separator"
echo


echo "$separator"
echo Тест 2: файлы не совпадают
bash ./comparator4.sh "./tests/file1.txt" "./tests/file2.txt" -v
echo Код возврата: "$?"
echo "$separator"
echo



echo "$separator"
echo Тест 3: Один из файлов отсутствует
bash ./comparator4.sh "./tests/notexist.txt" "./tests/file2.txt" -v
echo Код возврата: "$?"
echo "$separator"
echo


echo "$separator"
echo Тест 4: В одном из файлов отсутствуют ЧПТ
bash ./comparator4.sh "./tests/file1.txt" "./tests/file3.txt" -v
echo Код возврата: "$?"
echo "$separator"
echo



echo Тестирование варианта 4 завершено.