import os
import struct


def is_name_correct(name):
    if len(name) == 0:
        return False
    for i in ',<>:\'"/?|*\\':
        if i in name:
            return False
    return True


def is_file_name_correct(name):
    # print(name)
    tmp = name.split('.')
    # print(tmp)
    try:
        if not is_name_correct(tmp[0]) and len(tmp[0]) > 0:
            return False
    except:
        pass
    try:
        if not is_name_correct(tmp[1]):
            return False
    except:
        pass
    # for i in ':?.,!/\\':
    #     if i in tmp[0] or i in tmp[1]:
    #         return False
    return True


def is_correct_path(db_path):
    path = db_path.split('/')
    while '' in path:
        path.remove('')
    if len(path) <= 0:
        return False
    try:
        if not is_file_name_correct(path[-1]):
            raise Exception()
    except Exception:
        return False
    if path[0] == '..' or path[0] == '.' or path[0] == '':
        start = 1
    else:
        start = 0
    for i in range(start, len(path) - 1):
        if not is_name_correct(path[i]):
            return False

    return True


def check_file_exists(db_path):
    try:
        f = open(db_path, 'rb')
        f.close()
    except PermissionError:
        return PermissionError
    except FileNotFoundError:
        try:
            f = open(db_path, 'wb+')
            f.close()
            os.remove(db_path)
        except:
            return PermissionError
        return False
    return True


def input_with_params(input_text, error_text, expression):
    var = None
    while var is None:
        try:
            var = input(input_text)
            tmp = expression.split()
            tmp[tmp.index('var')] = str(var)
            tmp = ''.join(tmp)
            if eval(tmp):
                raise Exception()
        except:
            var = None
            print(error_text)
    return var


def line_generate(DB_FORMAT, i):
    num = int(input_with_params(
        input_text=f'Введите число номер {i+1}: ',
        error_text='Должно быть целое число',
        expression='not (" var ".isdigit())'
    ))
    structed_line = struct.pack(DB_FORMAT, num)
    return structed_line


def write_in_file(DB_FORMAT, db_path, n):
    # print(db_path)
    path = db_path.split('/')
    # print(path)
    if len(path) > 1:
        path = '/'.join(path[:-1])
        try:
            if not os.path.isdir(path):
                os.makedirs(path)
        except:
            pass
    # print(path)

    with open(db_path, 'w+b') as f:
        for i in range(n):
            f.write(line_generate(DB_FORMAT, i))


def get_db_line_count(DB_FORMAT, db_path):
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    with open(db_path, 'rb') as f:
        try:
            f.seek(0, os.SEEK_END)
            size = f.tell()
        except OSError:
            f.seek(0)
            size = f.tell()
    return size // LINE_SIZE
