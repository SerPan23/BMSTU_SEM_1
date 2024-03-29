# Паншин Сергей ИУ7-13Б
# Вариант 74

# Программа вычисляющая сумму бесконечного ряда
# z = 1 - 1/2 * x + ... + (-1)**n * (1*3*...*(2n-1)) * x**n / (2*4*...*(2*n))
# с точностью до члена ряда ε

import math as m

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

# для дроби
fract = 1

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

        # замена степени на умножение, чтобы проверить переполнение
        tmp = 1
        for j in range(i):
            tmp *= x

        if i > 0:
            fract *= (2*i-1)
            fract /= 2 * i
            fract *= -1

        current = fract * tmp

        z += current

        if m.isinf(z):
            finish_i = -2
            break

        if i % step == 0:
            print(f'| {i + 1:^12.5g} | {current:^12.5g} | {z:^12.5g} |')

        if abs(current) <= eps:
            finish_i = i + 1
            break

    print('-' * table_width)

    if finish_i == -2:
        print("Ошибка! Переполнение, указанной точности достичь не удалось")
    elif finish_i != -1:
        print(f'Сумма бесконечного ряда - {z:^.5g}, вычислена за {finish_i:^.5g} итерацию(й).')
    else:
        print('За указанное число итераций необходимой точности достичь не удалось.')
