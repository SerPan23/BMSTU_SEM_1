import file_worker


def finish_program():
    print('Программа завершена!')
    exit()


def choose_file():
    db_name = None
    while db_name is None:
        try:
            db_name = \
                input('Введите название файла, который хотиете выбрать (для разделения каталогов используйте /): ')
            if not file_worker.is_correct_path(db_name):
                db_name = None
                raise ValueError()
            tmp = file_worker.check_file_exists(db_name)
            if tmp == PermissionError:
                raise PermissionError()
            elif not file_worker.check_file_exists(db_name):
                raise Exception()
        except ValueError:
            print('Название файла должно иметь ввид demo.txt\nИ в названии файла не должны быть символы ,.<>:\'"/?|*\\')
        except PermissionError:
            print('Ошибка! У вас нет прав на открытие этого файла')
        except Exception:
            print('Файл с заданным именем не существует! Хотите его создать?')
            answer = None
            while answer is None:
                try:
                    answer = int(input('1 - создать\n0 - отмена\nВыберите что хотите сделать (0-1): '))
                    if not (0 <= answer <= 1):
                        answer = None
                        raise Exception()
                except:
                    print('Ответ должен быть целым числом от 0 до 1')
            if answer == 1:
                init_db(db_name)
                return db_name
            else:
                db_name = None
    return db_name


def line_generator(db_name):
    id = file_worker.get_last_id(db_name) + 1
    name = surname = second_name = None
    while name is None:
        try:
            name = input('Введите имя абитуриента: ')
            if len(name) <= 0:
                name = None
                raise Exception()
        except:
            print('Имя не может быть пустой строкой')
    while surname is None:
        try:
            surname = input('Введите фамилию абитуриента: ')
            if len(surname) <= 0:
                surname = None
                raise Exception()
        except:
            print('Фамилия не может быть пустой строкой')
    while second_name is None:
        try:
            second_name = input('Введите отчество абитуриента: ')
            if len(second_name) <= 0:
                second_name = None
                raise Exception()
        except:
            print('Отчество не может быть пустой строкой')
    sum_ege_results = None
    while sum_ege_results is None:
        try:
            sum_ege_results = int(input('Введите сумму баллов за егэ: '))
            if sum_ege_results < 0:
                sum_ege_results = None
                raise Exception()
        except:
            print('Сумма баллов за егэ должна быть положительным целым числом')
    additional_points = None
    while additional_points is None:
        try:
            additional_points = int(input('Введите сумму баллов за индивидуальные достижения: '))
            if additional_points < 0:
                additional_points = None
                raise Exception()
        except:
            print('Сумма баллов за индивидуальные достижения должна быть положительным целым числом')
    line = '|'.join([
        str(id),
        name,
        surname,
        second_name,
        str(sum_ege_results),
        str(additional_points),
    ])
    return line


def init_db(db_name):
    if file_worker.check_file_exists(db_name):
        print('Файл с таким именним существует!')
        print('Вы хотите его перезаписать? (данные будут утеряны)')
        answer = None
        while answer is None:
            try:
                answer = int(input('1 - перезаписать\n0 - отмена\nВыберите что хотите сделать (0-1): '))
                if not (0 <= answer <= 1):
                    answer = None
                    raise Exception()
            except:
                print('Ответ должен быть целым числом от 0 до 1')
        if answer == 0:
            return

    lines_count = None
    while lines_count is None:
        try:
            lines_count = int(input('Введите количество записей, которое хотите добавить при инициализации: '))
            if lines_count < 0:
                lines_count = None
                raise Exception()
        except:
            print('Количество записей должно быть целое число большее или равное 0')
    file_worker.create_file(db_name, [line_generator(db_name) for _ in range(lines_count)])


def print_line(line):
    data = line.rstrip().split('|')
    if len(data) < 6:
        tmp = ['None'] * 6
        for i in range(len(data)):
            tmp[i] = data[i]
        data = tmp
    print('| {:^5} | {:^25} | {:^25} | {:^25} | {:^20} | {:^35} |'.format(*data))


def show_db(db_name=None, lines=[]):
    tmp = '| {:^5} | {:^25} | {:^25} | {:^25} | {:^20} | {:^35} |' \
        .format("id", "Имя", "фамилия", "отчество",
                "сумма баллов за егэ", "баллы за индивидуальные достижения")
    width = len(tmp)
    print('-' * width)
    print(tmp)
    print('|' + '-' * (width - 2) + '|')
    if len(lines) == 0:
        with open(db_name, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                print_line(line)
    else:
        for line in lines:
            print_line(line)

    print('-' * width)


def add_line_in_db(db_name):
    file_worker.add_line(db_name, line_generator(db_name))


def search_id_col(db_name):
    id = None
    while id is None:
        try:
            id = int(input('Введите искомый id: '))
            if id < 0:
                id = None
                raise Exception()
        except:
            print('Искомый должен быть положительным целым числом')
    res = file_worker.search_by_id(db_name, id)
    if len(res) == 0:
        print('Строка с заданным id не найдена')
    else:
        show_db(lines=res)


def search_name_and_surname_cols(db_name):
    name = input('Введите имя абитуриента: ')
    surname = input('Введите фамилию абитуриента: ')
    res = file_worker.search_by_name_and_surname(db_name, name, surname)

    if len(res) == 0:
        print('Строка с заданным именем и фамилией не найдена')
    else:
        show_db(lines=res)
