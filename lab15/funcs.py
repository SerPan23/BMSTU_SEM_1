import struct

import file_worker as fw
import re


def choose_file():
    db_path = None
    while db_path is None:
        try:
            db_path = \
                input('Введите название файла, который хотиете выбрать (для разделения каталогов используйте /): ')
            if not fw.is_correct_path(db_path):
                db_path = None
                raise ValueError()
            tmp = fw.check_file_exists(db_path)
            if tmp == PermissionError:
                db_path = None
                raise PermissionError()
            elif not tmp:
                raise Exception()
        except ValueError:
            print('В названии файла не должны быть символы ,<>:\'"/?|*\\ и оно не должно быть пустым')
        except PermissionError:
            print('Ошибка! У вас нет прав на открытие этого файла')
        except Exception:
            print('Файл с заданным именем не существует! Он будет создан')
    return db_path


def add_nums(DB_FORMAT, path):
    n = int(fw.input_with_params(
        input_text='Введите количество чисел: ',
        error_text='Должно быть целое число больше 0',
        expression='int(" var ") <= 0'
    ))

    fw.write_in_file(DB_FORMAT, path, n)


def print_nums(DB_FORMAT, db_path):
    lines_count = fw.get_db_line_count(DB_FORMAT, db_path)
    if lines_count == 0:
        print('Файл пустой')
        return
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    ind = 0
    with open(db_path, 'rb') as f:
        while True:
            line = f.read(LINE_SIZE)
            if not line:
                break
            data = struct.unpack(DB_FORMAT, line)[0]
            print(f'{ind+1}-е число: {data}')
            ind += 1
