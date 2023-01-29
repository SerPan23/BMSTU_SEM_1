# Паншин Сергей ИУ7-13Б
# Даны 2 текстовых файла in1.txt и in2.txt.
# В первом файле записано N целых чисел со значениями от 1 до 3000 по одному в строке.
# Во втором файле записаны целые числа от 1 до N в произвольном порядке - номера строк в первом файле.
# Требуется сформировать файл out1.txt, в который записать числа из файла in1.txt,
# переведённые в римскую систему счисления, с выравниванием по центру
# (на основе длины числа с самым большим количеством цифр в римской с/с).
# Далее требуется сформировать файл out2.txt, переписав в него строки из файла out1.txt
# на основе порядка, заданного в файле in2.txt.
# Не разрешается считывать в память более одной строки каждого файла одновременно.

def convert_num_to_roman_num(num):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    thousand = m[num // 1000]
    hundred = c[(num % 1000) // 100]
    ten = x[(num % 100) // 10]
    one = i[num % 10]

    return thousand + hundred + ten + one


# Функция создает первый файл по заданию
def make_out1():
    max_len = 0
    with open('in1.txt', 'r') as inf:
        for line in inf:
            num = int(line)
            roman_num = convert_num_to_roman_num(num)
            max_len = max(len(roman_num), max_len)
    with open('out1.txt', 'w') as outf, open('in1.txt', 'r') as inf:
        for line in inf:
            num = int(line)
            roman_num = convert_num_to_roman_num(num)
            outf.write(f'{roman_num.center(max_len)}' + '\n')


# Функция создает второй файл по заданию
def make_out2():
    with open('out1.txt', 'rb') as out1f, open('in2.txt', 'r') as inf, open('out2.txt', 'w') as out2f:
        line_len = len(out1f.readline())
        for line in inf:
            pos = int(line) - 1
            out1f.seek(line_len * pos)
            out2f.write(out1f.read(line_len).decode())


make_out1()

make_out2()
