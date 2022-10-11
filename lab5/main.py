# Паншин Сергей ИУ7-13Б
# Вариант 74

# Программа вычисляющая сумму бесконечного ряда
# z = 1 - 1/2 * x + ... + (-1)**n * (1*3*...*(2n-1)) * x**n / (2*4*...*(2*n))
# с точностью до члена ряда ε

x = float(input('Введите значение аргумента: '))
eps = float(input('Введите точность: '))

# Проверка значиние точности
while True:
    if eps <= 0:
        print('Ошибка! Точность меньше либо равен нулю')
        eps = float(input('Введите точность: '))
    else:
        break

iter_count = int(input('Введите количество итераций: '))

# Проверка количества итераций
while True:
    if iter_count <= 0:
        print('Ошибка! Количество итераций меньше либо равено нулю')
        iter_count = int(input('Введите количество итераций: '))
    else:
        break

step = int(input('Введите шаг: '))

# Проверка шага
while True:
    if step <= 0:
        print('Ошибка! Шаг меньше либо равен нулю')
        step = int(input('Введите шаг: '))
    elif step >= iter_count:
        print('Ошибка! Шаг больше либо равен количеству итераций')
        step = int(input('Введите шаг: '))
    else:
        break

# текущее значение
current = 1

if abs(current) <= eps:
    print('Сумма бесконечного ряда - 0, вычислена за  1 итерацию.')
else:
    # сумма ряда
    z = 0
    # индекс окончания
    finish_i = -1
    # ширина таблицы
    table_width = 12 * 3 + 10
    print('-' * table_width)
    print(f'| {"№ итерации":^12} | {"t":^12} | {"s":^12} |')
    print('|' + '-' * (table_width - 2) + '|')
    for i in range(iter_count):

        # числитель
        numerator = 1
        for j in range(1, (2 * i - 1) + 1, 2):
            numerator *= j

        # знаменатель
        denominator = 1
        for j in range(2, 2 * i + 1, 2):
            denominator *= j

        current = (-1) ** i * (numerator / denominator) * x ** i

        z += current

        if i % step == 0:
            print(f'| {i + 1:^12.5g} | {current:^12.5g} | {z:^12.5g} |')

        if abs(current) <= eps:
            finish_i = i + 1
            break

    print('-' * table_width)

    if finish_i != -1:
        print(f'Сумма бесконечного ряда - {z:^.5g}, вычислена за {finish_i:^.5g} итерацию(й).')
    else:
        print('За указанное число итераций необходимой точности достичь не удалось.')
