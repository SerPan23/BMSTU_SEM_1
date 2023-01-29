# Паншин Сергей ИУ7-13Б
# Бинарный файл чисел удаляем нули
import os
import struct

format = 'l'
line_size = struct.calcsize(format)


def input_file(file_format, path, data):
    with open(path, 'wb') as f:
        for item in data:
            item_bin = struct.pack(file_format, item)
            f.write(item_bin)


def print_file(file_format, path):
    with open(path, 'rb') as f:
        while True:
            line_bin = f.read(line_size)
            if not line_bin:
                break
            line = struct.unpack(file_format, line_bin)[0]
            print(line)


def get_nums_count(path):
    with open(path, 'rb') as f:
        try:
            f.seek(0, os.SEEK_END)
            size = f.tell()
        except OSError:
            f.seek(0)
            size = f.tell()
    return size // line_size


def del_zero_from_file(file_format, path):
    nums_count = get_nums_count(path)
    with open(path, 'r+b') as f:
        count = 0
        for i in range(nums_count):
            f.seek(line_size * i)
            num_bin = f.read(line_size)
            num = struct.unpack(file_format, num_bin)[0]
            if num == 0:
                count += 1
            else:
                f.seek(line_size * (i - count))
                f.write(num_bin)
        f.truncate(os.path.getsize(path) - line_size * count)


file_path = input('Введите путь до файла: ')
n = int(input('Введите количество чисел: '))
data = [0] * n
for i in range(n):
    data[i] = int(input(f'Введите {i+1}-е число: '))


input_file(format, file_path, data)

del_zero_from_file(format, file_path)

n = get_nums_count(file_path)

if n == 0:
    print('Файл пустой')
else:
    print_file(format, file_path)
