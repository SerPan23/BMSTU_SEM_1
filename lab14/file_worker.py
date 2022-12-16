import os
import struct
import useful_funcs as uf


def is_name_correct(name):
    if len(name) == 0:
        return False
    for i in ',<>:\'"/?|*\\':
        if i in name:
            return False
    return True


def is_file_name_correct(name):
    # print(name)
    flag = ('.' in name)
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
    if len(path) <= 0:
        return False
    try:
        if not is_file_name_correct(path[-1]):
            raise Exception()
    except Exception:
        return False
    if path[0] == '..' or path[0] == '.':
        start = 1
    else:
        start = 0
    for i in range(start, len(path) - 1):
        if not is_name_correct(path[i]):
            return False

    return True


def check_file_exists(db_path):
    try:
        open(db_path, 'r')
    except PermissionError:
        return PermissionError
    except FileNotFoundError:
        try:
            f = open(db_path, 'w+')
            f.close()
            os.remove(db_path)
        except PermissionError:
            return PermissionError
        return False
    return True


def get_db_line_count(db_path, DB_FORMAT):
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    with open(db_path, 'rb') as f:
        try:
            f.seek(0, os.SEEK_END)
            size = f.tell()
        except OSError:
            f.seek(0)
            size = f.tell()
    return size // LINE_SIZE


def get_last_id(db_path, DB_FORMAT):
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    last_id = None
    try:
        with open(db_path, 'rb') as f:
            try:
                f.seek(0, os.SEEK_END)
                # print(f.tell())
                f.seek(-LINE_SIZE, os.SEEK_END)
                # print(f.tell())
            except OSError:
                f.seek(0)
            # print(f.tell())
            last_id = f.read(LINE_SIZE)
            # print(last_id)
            last_id = struct.unpack(DB_FORMAT, last_id)[0]
    except:
        pass
    if last_id is None or last_id == b'':
        return -1
    return int(last_id)


def clear_file(db_path):
    try:
        f = open(db_path, 'wb')
        f.close()
    except:
        pass


def create_file(db_path, lines=[]):
    path = db_path.split('/')
    path = '/'.join(path[:-1])
    # print(path)
    try:
        if not os.path.isdir(path):
            os.makedirs(path)
    except:
        pass

    # print(db_path)
    with open(db_path, 'w+b') as f:
        for line in lines:
            f.write(line)


def line_add(db_path, DB_FORMAT, line_index, lines_count, new_line):
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    with open(db_path, 'r+b') as f:
        try:
            f.seek(-LINE_SIZE, os.SEEK_END)

            while lines_count > line_index - 1:
                prev_chunk = f.read(LINE_SIZE)
                f.write(prev_chunk)
                if line_index == 1:
                    if lines_count - line_index != 0:
                        f.seek(-LINE_SIZE * 3, os.SEEK_CUR)
                    else:
                        f.seek(0)
                else:
                    f.seek(-LINE_SIZE * 3, os.SEEK_CUR)
                lines_count -= 1
        except:
            pass

        if lines_count == 0:
            f.seek(0)
        elif line_index != 1:
            f.seek(LINE_SIZE, os.SEEK_CUR)
        f.write(new_line)


def line_remove(db_path, DB_FORMAT, line_index):
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    with open(db_path, "r+b") as f:
        f.seek(LINE_SIZE * line_index)
        while True:
            line = f.read(LINE_SIZE)
            if not line:
                break
            f.seek(-LINE_SIZE * 2, os.SEEK_CUR)
            f.write(line)
            f.seek(LINE_SIZE, os.SEEK_CUR)

        f.truncate(os.path.getsize(db_path) - LINE_SIZE)


def search_by_ege_results(db_name, DB_FORMAT, sum_ege_results_need):
    found_lines = []
    with open(db_name, 'rb') as f:
        while True:
            LINE_SIZE = struct.calcsize(DB_FORMAT)
            line = f.read(LINE_SIZE)
            if not line:
                break

            line_data = struct.unpack(DB_FORMAT, line)
            try:
                tmp = line_data[3].rstrip(b'\x00').decode()
            except:
                tmp = line_data[3]
            if int(tmp) == int(sum_ege_results_need):
                found_lines.append(line)
    return found_lines


def search_by_name_and_surname_cols(db_name, DB_FORMAT, name, surname):
    found_lines = []
    with open(db_name, 'rb') as f:
        while True:
            LINE_SIZE = struct.calcsize(DB_FORMAT)
            line = f.read(LINE_SIZE)
            if not line:
                break

            line_data = struct.unpack(DB_FORMAT, line)
            try:
                tmp_name = line_data[0].rstrip(b'\x00').decode()
                tmp_surname = line_data[1].rstrip(b'\x00').decode()
            except:
                tmp_name = line_data[0]
                tmp_surname = line_data[1]
            if tmp_name == name and tmp_surname == surname:
                found_lines.append(line)
    return found_lines
