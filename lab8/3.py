# Паншин Сергей ИУ7-13Б
# Найти столбец, имеющий наименьшее количество отрицательных элементов.

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

need_column_ind = -1
min_count = -1

for j in range(column_count):
    count = 0
    for i in range(row_count):
        if matrix[i][j] < 0:
            count += 1
    if min_count == -1 and count > 0:
        need_column_ind = j
        min_count = count
    elif min_count > count > 0:
        need_column_ind = j
        min_count = count


if need_column_ind == -1:
    print('Нужный столбец не найден')
else:
    print(f'Столбец с наименьшом количеством отрицательных элементов имеет индекс = {need_column_ind}')
    print('Элементы данной столбца: ')
    for i in range(row_count):
        print(f'{j+1}-й элемент: {matrix[i][need_column_ind]}')
