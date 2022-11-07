# Паншин Сергей ИУ-13Б
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G.

row_count = int(input('Введите количество строк матриц D и Z: '))
column_count = int(input('Введите количество столбцов матриц D и Z: '))

while row_count <= 0 or column_count <= 0:
    print('Ошибка количество строк и столбцов должен быть больше 0')
    row_count = int(input('Введите количество строк матриц D и Z: '))
    column_count = int(input('Введите количество столбцов матриц D и Z: '))

matrix_d = [[0]*column_count for _ in range(row_count)]

print('Введите элементы матрицы D:')
for i in range(row_count):
    for j in range(column_count):
        matrix_d[i][j] = int(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))


matrix_z = [[0]*column_count for _ in range(row_count)]

print('Введите элементы матрицы Z:')
for i in range(row_count):
    for j in range(column_count):
        matrix_z[i][j] = int(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))


print('Матрица Z:')
tmp = f'{"i/j":^4}|'
for j in range(column_count):
    tmp += f'{j+1:^6}|'
width = len(tmp)
print('-' * width)
print(tmp)
print('-' * width)
for i in range(row_count):
    tmp = f'{i+1:^4}|'
    for j in range(column_count):
        tmp += f'{matrix_z[i][j]:^6}|'
    print(tmp)
print('-' * width)

g = [0] * row_count

for i in range(row_count):
    sum_i_z = sum(matrix_z[i])
    for j in range(column_count):
        if matrix_d[i][j] > sum_i_z:
            g[i] += 1

print('Матрица G до преобразований:')
tmp = f'{"i/j":^4}|'
for j in range(column_count):
    tmp += f'{j+1:^6}|'
width = len(tmp)
print('-' * width)
print(tmp)
print('-' * width)
for i in range(row_count):
    tmp = f'{i+1:^4}|'
    for j in range(column_count):
        tmp += f'{matrix_d[i][j]:^6}|'
    print(tmp)
print('-' * width)

max_g = max(g)

for i in range(row_count):
    for j in range(column_count):
        matrix_d[i][j] *= max_g

print('Матрица G после преобразований:')
tmp = f'{"i/j":^4}|'
for j in range(column_count):
    tmp += f'{j+1:^6}|'
width = len(tmp)
print('-' * width)
print(tmp)
print('-' * width)
for i in range(row_count):
    tmp = f'{i+1:^4}|'
    for j in range(column_count):
        tmp += f'{matrix_d[i][j]:^6}|'
    print(tmp)
print('-' * width)

print('Массив G:')
for i in range(row_count):
    print(f'{i + 1}-й элемент массива g: {g[i]}')

