# Паншин Сергей ИУ7-13Б
# Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов


row_count = int(input('Введите количество строк: '))
column_count = int(input('Введите количество столбцов: '))

matrix = [[0]*column_count for _ in range(row_count)]

for i in range(row_count):
    for j in range(column_count):
        matrix[i][j] = int(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))


max_str_ind = -1
min_str_ind = -1
max_count = 0
min_count = -1

for i in range(row_count):
    count = 0
    for j in range(column_count):
        if matrix[i][j] < 0:
            count += 1

    if min_str_ind == -1 and count > 0:
        min_str_ind = i
        min_count = count
    elif min_count > count > 0:
        min_str_ind = i
        min_count = count

    if max_count < count:
        max_count = count
        max_str_ind = i

if max_str_ind == 1 or min_str_ind == -1:
    print('Нужные строки не найдены')
else:
    matrix[max_str_ind], matrix[min_str_ind] = matrix[min_str_ind], matrix[max_str_ind]
    tmp = f'{"":<3} '
    for j in range(column_count):
        tmp += f'{j+1:^6}'
    print(tmp)
    for i in range(row_count):
        tmp = f'{i+1:<3} '
        for j in range(column_count):
            tmp += f'{matrix[i][j]:^6}'
        print(tmp)


