# Паншин Сергей ИУ7-13Б
# Найти строку, имеющую наибольшее количество чётных элементов.

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

need_str_ind = -1            # нужная строка
max_count = 0                # макс количество

for i in range(row_count):
    count = 0
    for j in range(column_count):
        if matrix[i][j] % 2 == 0:
            count += 1

    if count > max_count:
        need_str_ind = i
        max_count = count

if need_str_ind == -1:
    print('Нужая строка не найдена')
else:
    print(f'Строка с наибольшим количеством четных элементов имеет индекс = {need_str_ind}')
    print('Элементы данной строки: ')
    for j in range(len(matrix[need_str_ind])):
        print(f'{j+1}-й элемент: {matrix[need_str_ind][j]}')

