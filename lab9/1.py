# Паншин Сергей ИУ-13Б
# Даны массивы D и F. Сформировать матрицу A по формуле
# ajk = sin(dj+fk).
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и рядом столбцы AV и L.

import math as m

dn = int(input('Введите размера массива d: '))
d = [0.0] * dn
for i in range(dn):
    d[i] = float(input(f'Введите {i+1}-й элемент массива d: '))

fn = int(input('Введите размера массива f: '))
f = [0.0] * fn
for i in range(fn):
    f[i] = float(input(f'Введите {i+1}-й элемент массива f: '))

a = [[0.0] * fn for _ in range(dn)]

av = [0.0] * dn

for j in range(dn):
    sum_positive = 0
    count_positive = 0
    for k in range(fn):
        a[j][k] = m.sin(d[j] + f[k])

        if a[j][k] > 0:
            sum_positive += a[j][k]
            count_positive += 1

    if count_positive > 0:
        av[j] = sum_positive / count_positive
    else:
        av[j] = None

l = [0] * dn
for j in range(dn):
    for k in range(fn):
        if av[j] is not None and a[j][k] < av[j]:
            l[j] += 1


tmp = f'{"i/j":^4}|'
for j in range(fn):
    tmp += f'{j+1:^16}|'
tmp += f'{"AV":^16}|'
tmp += f'{"L":^16}|'
width = len(tmp)
print('-' * width)
print(tmp)
print('-' * width)
for i in range(dn):
    tmp = f'{i+1:^4}|'
    for j in range(fn):
        tmp += f'{a[i][j]:^16.5g}|'
    if av[i] is not None:
        tmp += f'{av[i]:^16.5g}|'
    else:
        tmp += f'{"Неопределенно":^16}|'
    tmp += f'{l[i]:^16.5g}|'
    print(tmp)
print('-' * width)
