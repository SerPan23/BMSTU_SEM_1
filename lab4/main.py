# Паншин Сергей ИУ7-13Б
# Вариант 15

# Программа, которая для заданных функций (h1 = a^2 + 4sin(a) и
# h2 = e^a + e^(-1.5 * a) - 4) выводит таблицу значений этих
# функций на некотором отрезке. Запрашивает кол-во засечек и строит график одной из них (h1).

import math as m

start_a = float(input('Введите начальное значение аргумента: '))
end_a = float(input('Введите конечное значение аргумента: '))
step_a = float(input('Введите шаг разбиения данного отрезка: '))

for _ in range(100*1000):
    if start_a >= end_a:
        print('Начальное значение не может быть больше или равно конечному')
        start_a = float(input('Введите начальное значение аргумента: '))
        end_a = float(input('Введите конечное значение аргумента: '))
    elif step_a <= 0:
        print('Шаг не может быть меньше или равнен нулю')
        step_a = float(input('Введите шаг разбиения данного отрезка: '))
    elif end_a - start_a < step_a:
        print('Шаг не может быть больше разницы конечного и начального значения аргумента')
        step_a = float(input('Введите шаг разбиения данного отрезка: '))
    else:
        break

eps = 1e-8
a = start_a
n = round(abs(end_a - start_a) / step_a) + 1
h1_min = float('+inf')
h1_max = float('-inf')
h2_min = float('+inf')

# вывод таблицы
print("-" * 46)
print(f'| {"a":^12} | {"h1":^12} | {"h2":^12} |')
print("-" * 46)
for _ in range(n):
    h1 = a ** 2 + 4 * m.sin(a)
    h2 = m.e ** a + m.e ** (-1.5 * a) - 4
    h1_min = min(h1_min, h1)
    h1_max = max(h1_max, h1)
    h2_min = min(h2_min, h2)

    print(f'| {a:^12.5g} | {h1:^12.5g} | {h2:^12.5g} |')
    a += step_a
print("-" * 46, end='\n\n')

scale = int(input('Введите количество засечек: '))  # кол-во засечек
for _ in range(100*1000):
    if not(4 <= scale <= 8):
        print('Количество засечек должно быть от 4 до 8')
        scale = int(input('Введите количество засечек: '))
    else:
        break

delta = (h1_max - h1_min)/(scale - 1)               # число между засечками
width = 100                                         # ширина поля
point_scale = width / (h1_max - h1_min)             # коэффицент маштаба на поле
spaces_between = (width - scale * 12)/(scale - 1)   # кол-во пробелов между засечек
chart_header = ' ' * 13                             # заголовок графика
h = h1_min

# формирование заголовка графика
for i in range(scale):
    if i == scale - 1:
        chart_header += f'{h: >12.5g}'
    elif i == scale - 2:
        chart_header += f'{h: <12.5g}' + ' ' * int(spaces_between) \
             + ' ' * (width - (int(spaces_between) * (scale - 1) + 12 * scale))
    else:
        chart_header += f'{h: <12.5g}' + ' ' * int(spaces_between)

    h += delta

print(chart_header)

# количества пробелов до OX
ox = 12 + (int(point_scale * (0 - h1_min)) - 1)

a = start_a

for _ in range(n):
    h = a ** 2 + 4 * m.sin(a)

    # количества пробелов до звездочки
    spaces_before = (int(point_scale * (h - h1_min)) - 1)

    # количества пробелов после звездочки
    spaces_after = (width - 11 - int(point_scale * (h - h1_min)) - 1)

    # график пересекает ОX
    if h1_min <= 0 <= h1_max:
        s = f'{a:<12.5g}|' + ' ' * spaces_before + '*' + ' ' * spaces_after
        if s[ox] != '*':
            s = s[:ox] + '|' + s[ox + 1:]
        print(s)
    # график непересекает ОX
    else:
        if abs(a) < eps:
            print(f'{0.0:<12.5g}|' + ' ' * spaces_before + '*' + ' ' * spaces_after)
        else:
            print(f'{a:<12.5g}|' + ' ' * spaces_before + '*' + ' ' * spaces_after)

    a += step_a

print('\n')
print(f'Минимальное значение h1 = {h1_min:.5g}')
print(f'Минимальное значение h2 = {h2_min:.5g}')
