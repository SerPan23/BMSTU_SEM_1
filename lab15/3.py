# Паншин Сергей ИУ7-13Б
# Сортировка методом вставок с бинарным поиском, бинарного файла с 32 битными числами
import struct

import funcs


def binary_search(DB_FORMAT, path, item, low, high):
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    with open(path, "r+b") as f:
        while low <= high:
            mid = low + (high - low) // 2
            # data[mid]
            f.seek(LINE_SIZE * mid)
            mid_num_bin = f.read(LINE_SIZE)
            mid_num = struct.unpack(DB_FORMAT, mid_num_bin)[0]
            if item == mid_num:
                return mid + 1
            elif item > mid_num:
                low = mid + 1
            else:
                high = mid - 1
    return low


def sort(DB_FORMAT, path):
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    nums_count = funcs.fw.get_db_line_count(DB_FORMAT, path)
    with open(path, "r+b") as f:
        for i in range(nums_count):
            j = i - 1
            # selected = data[i]
            f.seek(LINE_SIZE * i)
            selected_bin = f.read(LINE_SIZE)
            selected = struct.unpack(DB_FORMAT, selected_bin)[0]

            insert_loc = binary_search(DB_FORMAT, path, selected, 0, j)

            while j >= insert_loc:
                # data[j + 1] = data[j]
                f.seek(LINE_SIZE * j)
                num_bin = f.read(LINE_SIZE)
                f.seek(LINE_SIZE * (j + 1))
                f.write(num_bin)
                j -= 1
            # data[j + 1] = selected
            f.seek(LINE_SIZE * (j + 1))
            f.write(selected_bin)


DB_FORMAT = 'l'

path = funcs.choose_file()

funcs.add_nums(DB_FORMAT, path)

sort(DB_FORMAT, path)

funcs.print_nums(DB_FORMAT, path)
