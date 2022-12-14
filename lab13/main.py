# Паншин Сергей ИУ7-13Б
# Работа с бд с разделителями
# Функционал:
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
# его записями)
# 3. Вывести содержимое базы данных
# 4. Добавить запись в конец базы данных
# 5. Поиск по одному полю (id)
# 6. Поиск по двум полям (name, surname)

# Разделитель БД = |
# Поля БД:
# - id                  неповторяющийся в таблице номер (генерируется сам при создании строки)
# - name                имя абитуриента
# - surname             фамилия абитуриента
# - second_name         отчество абитуриента
# - sum_ege_results     сумма всех баллов за егэ
# - additional_points   баллы за индивидуальные достижения


from funcs import *

db_name_use = None

def menu():
    funcs = [
        finish_program,
        choose_file,
        init_db,
        show_db,
        add_line_in_db,
        search_id_col,
        search_name_and_surname_cols,
    ]
    text = [
        'Меню:',
        '1) Выбрать файл для работы',
        '2) Инициализировать базу данных',
        '3) Вывести содержимое базы данных',
        '4) Добавить запись в конец базы данных',
        '5) Поиск по одному полю (id)',
        '6) Поиск по двум полям (name, surname)',
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
            if not (0 <= item_selected_number < 7):
                item_selected_number = None
                raise ValueError()
        except ValueError:
            print('-' * 50)
            print('Номер операции должен быть целым числом от 0 до 6')
            print('-' * 50)

    global db_name_use
    if item_selected_number == 0:
        funcs[0]()
    elif item_selected_number == 1:
        db_name_use = funcs[1]()
    else:
        print('-' * 50)
        if db_name_use is None:
            print('Ошибка выберите сначала бд с которой будете работать (пункт 1)')
        else:
            funcs[item_selected_number](db_name_use)


while True:
    menu()

# tmp = choose_file()
# print(tmp)
# show_db(tmp)
# add_line_in_db(tmp)
# show_db(tmp)