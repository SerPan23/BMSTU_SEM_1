# Паншин Сергей ИУ7-13Б
# Удалить все нечётные элементы, за один проход
# по бинарному файлу с 32 битными числами

import os
import struct

import funcs


def del_nums(DB_FORMAT, path):
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    nums_count = funcs.fw.get_db_line_count(DB_FORMAT, path)
    count = 0
    with open(path, "r+b") as f:
        for i in range(nums_count):
            f.seek(LINE_SIZE * i)
            num_bin = f.read(LINE_SIZE)
            num = struct.unpack(DB_FORMAT, num_bin)[0]
            if num % 2 != 0:
                count += 1
            else:
                f.seek(LINE_SIZE * (i - count))
                f.write(num_bin)
        f.truncate(os.path.getsize(path) - LINE_SIZE * count)



DB_FORMAT = 'l'

path = funcs.choose_file()

print(path)

funcs.add_nums(DB_FORMAT, path)

del_nums(DB_FORMAT, path)

funcs.print_nums(DB_FORMAT, path)
