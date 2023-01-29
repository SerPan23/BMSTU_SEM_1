# Паншин Сергей ИУ7-13Б
# После каждого чётного элемента, добавить его удвоенное
# значение (допускается два прохода по файлу) в бинарном файле с 32 битными числами.
import os
import struct
import funcs


def add_need_nums(DB_FORMAT, path):
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    nums_count = funcs.fw.get_db_line_count(DB_FORMAT, path)
    count = 0
    with open(path, "r+b") as f:
        for i in range(nums_count):
            f.seek(LINE_SIZE * i)
            num_bin = f.read(LINE_SIZE)
            num = struct.unpack(DB_FORMAT, num_bin)[0]
            if num % 2 == 0:
                count += 1
        for i in range(count):
            f.seek(0, os.SEEK_END)
            f.write(struct.pack(DB_FORMAT, 0))

    with open(path, "r+b") as f:
        end_ind = nums_count - 1 + count
        for i in range(nums_count - 1, -1, -1):
            f.seek(LINE_SIZE * i)
            num_bin = f.read(LINE_SIZE)
            num = struct.unpack(DB_FORMAT, num_bin)[0]
            if num % 2 == 0:
                # a[end_ind] = a[i] * 2
                f.seek(LINE_SIZE * end_ind)
                f.write(struct.pack(DB_FORMAT, num * 2))
                # a[end_ind - 1] = a[i]
                f.seek(LINE_SIZE * (end_ind - 1))
                f.write(struct.pack(DB_FORMAT, num))
                end_ind -= 2
            else:
                # a[end_ind] = a[i]
                f.seek(LINE_SIZE * end_ind)
                f.write(struct.pack(DB_FORMAT, num))
                end_ind -= 1


DB_FORMAT = 'l'

path = funcs.choose_file()

funcs.add_nums(DB_FORMAT, path)

add_need_nums(DB_FORMAT, path)

funcs.print_nums(DB_FORMAT, path)
