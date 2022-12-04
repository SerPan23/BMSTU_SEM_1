import os


def is_name_correct(name):
    for i in '<>:"/?|*\\':
        if i in name:
            return False
    return True


def is_file_name_correct(name):
    tmp = name.split('.')
    if len(tmp) != 2:
        return False
    if not is_name_correct(tmp[0]) or not is_name_correct(tmp[1]):
        return False
    # for i in ':?.,!/\\':
    #     if i in tmp[0] or i in tmp[1]:
    #         return False
    return True


def is_correct_path(db_name):
    path = db_name.split('/')
    if len(path) <= 0:
        return False
    try:
        if not is_file_name_correct(path[-1]):
            raise Exception()
    except Exception:
        return False
    if path[0] == '..':
        start = 1
    else:
        start = 0
    for i in range(start, len(path) - 1):
        if not is_name_correct(path[i]):
            return False

    return True


def create_file(db_name, lines=None):
    path = db_name.split('/')
    path = '/'.join(path[:-1])
    if not os.path.isdir(path):
        os.makedirs(path)

    if lines is None:
        lines = []
    print(db_name)
    with open(db_name, 'w+') as f:
        for line in lines:
            f.write(line)


def check_file_exists(db_name):
    try:
        open(db_name, 'r')
    except Exception:
        return False
    return True


def get_last_id(db_name):
    last_id = None
    try:
        with open(db_name, 'rb') as f:
            try:
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            last_id = f.readline().decode().split('|')[0]
    except:
        pass
    if last_id is None or last_id == '':
        return -1
    return int(last_id)


def add_line(db_name, line):
    with open(db_name, 'a') as f:
        f.write(line + '\n')


def del_line(db_name, id):
    with open(db_name, 'r') as f:
        lines = f.readlines()
    with open(db_name, 'w') as f:
        for line in lines:
            if int(line.split('|')[0]) == id:
                continue
            f.write(line)


def search_by_id(db_name, id):
    found_lines = []
    if id > get_last_id(db_name):
        return found_lines
    with open(db_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break

            tmp_id = int(line.split('|')[0])
            if tmp_id == id:
                found_lines.append(line)
    return found_lines


def search_by_name_and_surname(db_name, name, surname):
    found_lines = []
    with open(db_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break

            tmp_line = line.split('|')
            if tmp_line[1] == name and tmp_line[2] == surname:
                found_lines.append(line)
    return found_lines
