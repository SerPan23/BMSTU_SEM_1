# Паншин Сергей ИУ-13Б
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.



row_count = int(input('Введите количество строк матрицы: '))
column_count = int(input('Введите количество столбцов матрицы: '))

while row_count <= 0 or column_count <= 0:
    print('Ошибка количество строк и столбцов должен быть больше 0')
    row_count = int(input('Введите количество строк матрицы: '))
    column_count = int(input('Введите количество столбцов матрицы: '))

matrix = [[0]*column_count for _ in range(row_count)]

for i in range(row_count):
    for j in range(column_count):
        matrix[i][j] = int(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))

ni = int(input('Введите размера массива i: '))
mass_i = [0] * ni

for i in range(ni):
    tmp = int(input(f'Введите {i+1}-й элемент массива i: '))
    while not(0 < tmp <= row_count):
        print("Ошибка! Индекс должен быть с 1 до количества строк")
        tmp = int(input(f'Введите {i + 1}-й элемент массива i: '))
    mass_i[i] = tmp

r = [0] * ni
sum_r = 0
count_r = 0
for i in enumerate(mass_i):
    r[i[0]] = max(matrix[i[1]-1])
    sum_r += r[i[0]]
    count_r += 1


if count_r > 0:
    av = sum_r/count_r

    print('Матрица D:')
    tmp = f'{"i/j":^4}|'
    for j in range(column_count):
        tmp += f'{j + 1:^6}|'
    width = len(tmp)
    print('-' * width)
    print(tmp)
    print('-' * width)
    for i in range(row_count):
        tmp = f'{i + 1:^4}|'
        for j in range(column_count):
            tmp += f'{matrix[i][j]:^6}|'
        print(tmp)
    print('-' * width)

    print('Массив I:')
    for i in range(ni):
        print(f'{i + 1}-й элемент массива g: {mass_i[i]}')

    print('Массив R:')
    for i in range(ni):
        print(f'{i + 1}-й элемент массива g: {r[i]}')

    print(f'Найденое среднее арифметическое значение = {av:.5g}')
else:
    print('Ни один максимум не найден')
