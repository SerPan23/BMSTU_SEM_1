# Паншин Сергей ИУ7-13Б
# Работа с бд с разделителями
# Функционал:
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
# его записями)
# 3. Вывести содержимое базы данных
# 4. Добавить запись в произвольное место базы данных (пользователь указывает
# номер позиции, в которую должна быть вставлена запись)
# 5. Удалить произвольную запись из базы данных (пользователь указывает номер
# удаляемой записи)
# 6. Поиск по одному полю (name)
# 7. Поиск по двум полям (name, surname)

# Поля БД:
# - name                имя абитуриента
# - surname             фамилия абитуриента
# - second_name         отчество абитуриента
# - sum_ege_results     сумма всех баллов за егэ
# - additional_points   баллы за индивидуальные достижения

from funcs import *

DB_FORMAT = '20s20s20sii'


def menu(db_path):
    funcs = [
        finish_program,
        choose_file,
        init_db,
        show_db,
        add_line_in_db,
        del_line_from_db,
        search_sum_ege_results_col,
        search_name_and_surname_cols,
    ]
    text = [
        'Используемый файл: ' + str(db_path),
        'Меню:',
        '1) Выбрать файл для работы',
        '2) Инициализировать базу данных',
        '3) Вывести содержимое базы данных',
        '4) Добавить запись в произвольное место базы данных',
        '5) Удалить произвольную запись из базы данных',
        '6) Поиск по одному полю (сумма баллов за егэ)',
        '7) Поиск по двум полям (имя, фамилия)',
        '0) Завершить программу',
    ]
    print('-' * 50)
    print(*text, sep='\n')
    print('-' * 50)
    item_selected_number = None
    while item_selected_number is None:
        try:
            item_selected_number = int(
                input('Введите номер операции которую хотите выполнить: '))
            if not (0 <= item_selected_number <= 7):
                item_selected_number = None
                raise ValueError()
        except ValueError:
            print('-' * 50)
            print('Номер операции должен быть целым числом от 0 до 7')
            print('-' * 50)

    if item_selected_number == 0:
        funcs[0]()
    elif item_selected_number == 1:
        db_path = funcs[1](DB_FORMAT)
    else:
        print('-' * 50)
        if db_path is None:
            print('Ошибка выберите сначала бд с которой будете работать (пункт 1)')
        else:
            funcs[item_selected_number](db_path, DB_FORMAT)
    return db_path


def main():
    db_path = None
    while True:
        db_path = menu(db_path)


if __name__ == '__main__':
    main()

# print(fw.get_db_line_count('./1.txt', DB_FORMAT))

# print(uf.input_with_params(
#         'Введите имя абитуриента: ',
#         'Имя не может быть пустой строкой и больше 255 символов',
#         'not (0 < len(" var ") <= 255)'
#     ))

# print(uf.input_with_params(
#         'Введите имя абитуриента: ',
#         'Имя не может быть пустой строкой',
#         'len(" var ") <= 0'
#     ))

# print(uf.input_with_params(
#         '1 - перезаписать\n0 - отмена\nВыберите что хотите сделать (0-1): ',
#         'Ответ должен быть целым числом от 0 до 1',
#         'not (0 <= int(" var ") <= 1)'
#     ))

# s = line_generate('fdf', DB_FORMAT)
# print(s)
# print(struct.unpack(DB_FORMAT, s))
# print(LINE_SIZE)
