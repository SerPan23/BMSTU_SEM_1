# Паншин Сергей ИУ7-13Б
# Переставить местами столбцы с максимальной и минимальной суммой
# элементов

row_count = int(input('Введите количество строк: '))
column_count = int(input('Введите количество столбцов: '))

while row_count <= 0 or column_count <= 0:
    print('Ошибка размер должен быть больше 0')
    row_count = int(input('Введите количество строк: '))
    column_count = int(input('Введите количество столбцов: '))

matrix = [[0]*column_count for _ in range(row_count)]

for i in range(row_count):
    for j in range(column_count):
        matrix[i][j] = int(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))


max_column_ind = -1                     # максимальный нужный столбец
min_column_ind = -1                     # минимальный нужный столбец
max_sum = 0
min_sum = 0

for j in range(column_count):
    s = 0
    for i in range(row_count):
        s += matrix[i][j]

    if max_sum < s:
        max_sum = s
        max_column_ind = j

    if min_column_ind == -1 and s > 0:
        min_sum = s
        min_column_ind = j
    elif min_sum > s > 0:
        min_sum = s
        min_column_ind = j


if max_column_ind == -1 or min_column_ind == -1:
    print('Нужные столбцы не найдены')
else:
    for i in range(row_count):
        matrix[i][min_column_ind], matrix[i][max_column_ind] = \
            matrix[i][max_column_ind], matrix[i][min_column_ind]

    tmp = f'{"":<3} '
    for j in range(column_count):
        tmp += f'{j + 1:^6}'
    print(tmp)
    for i in range(row_count):
        tmp = f'{i + 1:<3} '
        for j in range(column_count):
            tmp += f'{matrix[i][j]:^6}'
        print(tmp)
