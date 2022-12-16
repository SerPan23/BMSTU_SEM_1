import os

import file_worker as fw
import struct
import useful_funcs as uf


def finish_program():
    print('Программа завершена!')
    exit()


def choose_file(DB_FORMAT):
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
            print('В названии файла не должны быть символы ,<>:\'"/?|*\\')
        except PermissionError:
            print('Ошибка! У вас нет прав на открытие этого файла')
        except Exception:
            print('Файл с заданным именем не существует! Хотите его создать?')
            answer = uf.input_with_params(
                '1 - создать\n0 - отмена\nВыберите что хотите сделать (0-1): ',
                'Ответ должен быть целым числом от 0 до 1',
                'not (0 <= int(" var ") <= 1)'
            )
            if int(answer) == 1:
                init_db(db_path, DB_FORMAT)
                return db_path
            else:
                db_path = None
    return db_path


def init_db(db_path, DB_FORMAT):
    if fw.check_file_exists(db_path):
        print('Файл с таким именним существует!')
        print('Вы хотите его перезаписать? (данные будут утеряны)')
        answer = uf.input_with_params(
            '1 - перезаписать\n0 - отмена\nВыберите что хотите сделать (0-1): ',
            'Ответ должен быть целым числом от 0 до 1',
            'not (0 <= int(" var ") <= 1)'
        )
        if int(answer) == 0:
            return
    fw.clear_file(db_path)
    lines_count = int(uf.input_with_params(
        'Введите количество записей, которое хотите добавить при инициализации: ',
        'Количество записей должно быть целое число большее или равное 0',
        'int(" var ") < 0'
    ))

    fw.create_file(db_path, [line_generate(DB_FORMAT) for _ in range(lines_count)])


def input_line_data():
    name = uf.input_with_params(
        'Введите имя абитуриента: ',
        'Имя не может быть пустой строкой и больше 20 символов',
        'not (0 < len(" var ") <= 20)'
    )
    surname = uf.input_with_params(
        'Введите фамилию абитуриента: ',
        'Фамилия не может быть пустой строкой и больше 20 символов',
        'not (0 < len(" var ") <= 20)'
    )
    second_name = uf.input_with_params(
        'Введите отчество абитуриента(если его нет введите -): ',
        'Отчество не может быть пустой строкой и больше 20 символов',
        'not (0 < len(" var ") <= 20)'
    )
    sum_ege_results = uf.input_with_params(
        'Введите сумму баллов за егэ: ',
        'Сумма баллов за егэ должна быть положительным целым числом',
        'int(" var ") < 0'
    )
    additional_points = uf.input_with_params(
        'Введите сумму баллов за индивидуальные достижения: ',
        'Сумма баллов за индивидуальные достижения должна быть положительным целым числом',
        'int(" var ") < 0'
    )
    return name.encode(), surname.encode(), second_name.encode(), \
           int(sum_ege_results), int(additional_points)


def line_generate(DB_FORMAT):
    structed_line = struct.pack(DB_FORMAT, *input_line_data())
    return structed_line


def print_line(line, DB_FORMAT, ind):
    data = struct.unpack(DB_FORMAT, line)
    if len(data) <= 5:
        tmp = ['None'] * 5
        for i in range(len(data)):
            try:
                tmp[i] = data[i].rstrip(b'\x00').decode()
            except:
                tmp[i] = data[i]
        data = tmp
    print('| {:^5} | {:^25} | {:^25} | {:^25} | {:^20} | {:^35} |'.format(str(ind), *data))


def show_db(db_path, DB_FORMAT, lines=[]):
    lines_count = fw.get_db_line_count(db_path, DB_FORMAT)
    if lines_count == 0:
        print('База данных пустая')
        return
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    tmp = '| {:^5} | {:^25} | {:^25} | {:^25} | {:^20} | {:^35} |' \
        .format("№", "Имя", "фамилия", "отчество",
                "сумма баллов за егэ", "баллы за индивидуальные достижения")
    width = len(tmp)
    print('-' * width)
    print(tmp)
    print('|' + '-' * (width - 2) + '|')
    ind = 1
    if len(lines) == 0:
        with open(db_path, 'rb') as f:
            while True:
                line = f.read(LINE_SIZE)
                if not line:
                    break
                print_line(line, DB_FORMAT, ind)
                ind += 1
    else:
        for line in lines:
            print_line(line, DB_FORMAT, ind)
            ind += 1

    print('-' * width)


def add_line_in_db(db_path, DB_FORMAT):
    lines_count = fw.get_db_line_count(db_path, DB_FORMAT)
    if lines_count == 0:
        tmp = lines_count + 1
    else:
        tmp = lines_count
    line_index = int(uf.input_with_params(
        f'Введите номер строки куда хотите вставить (строки под сдвинутся вниз) (от 1 до {tmp}): ',
        'Сумма баллов за егэ должна быть положительным целым числом',
        f'not (0 < int(" var ") <= {tmp})'
    ))
    new_line = line_generate(DB_FORMAT)
    fw.line_add(db_path, DB_FORMAT, line_index, lines_count, new_line)


def del_line_from_db(db_path, DB_FORMAT):
    lines_count = fw.get_db_line_count(db_path, DB_FORMAT)
    if lines_count == 0:
        print('База данных пустая')
        return
    line_index = int(uf.input_with_params(
        f'Введите номер строки которую хотите удалить (от 1 до {lines_count}): ',
        'Сумма баллов за егэ должна быть положительным целым числом',
        f'not (0 < int(" var ") <= {lines_count})'
    ))
    fw.line_remove(db_path, DB_FORMAT, line_index)


def search_sum_ege_results_col(db_path, DB_FORMAT):
    sum_ege_results_need = uf.input_with_params(
        'Введите искомую сумму баллов за егэ: ',
        'Сумма баллов за егэ должна быть положительным целым числом',
        'int(" var ") < 0'
    )
    res = fw.search_by_ege_results(db_path, DB_FORMAT, sum_ege_results_need)
    if len(res) == 0:
        print('Ни одна строка с заданной суммой не найдена')
    else:
        show_db(db_path, DB_FORMAT, lines=res)


def search_name_and_surname_cols(db_path, DB_FORMAT):
    name = uf.input_with_params(
        'Введите имя абитуриента: ',
        'Имя не может быть пустой строкой и больше 20 символов',
        'not (0 < len(" var ") <= 20)'
    )
    surname = uf.input_with_params(
        'Введите фамилию абитуриента: ',
        'Фамилия не может быть пустой строкой и больше 20 символов',
        'not (0 < len(" var ") <= 20)'
    )
    res = fw.search_by_name_and_surname_cols(db_path, DB_FORMAT, name, surname)
    if len(res) == 0:
        print('Ни одна строка с заданным именем и фамилей не найдена')
    else:
        show_db(db_path, DB_FORMAT, lines=res)
