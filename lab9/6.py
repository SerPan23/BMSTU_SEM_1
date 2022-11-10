# Паншин Сергей ИУ-13Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V.

row_count = int(input('Введите количество строк матрицы: '))
column_count = int(input('Введите количество столбцов матрицы: '))

while row_count <= 0 or column_count <= 0:
    print('Ошибка количество строк и столбцов должен быть больше 0')
    row_count = int(input('Введите количество строк матрицы: '))
    column_count = int(input('Введите количество столбцов матрицы: '))


matrix_a = [[0.0]*column_count for _ in range(row_count)]
print('Матрица A:')
for i in range(row_count):
    for j in range(column_count):
        matrix_a[i][j] = float(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))

matrix_b = [[0.0]*column_count for _ in range(row_count)]
print('Матрица B:')
for i in range(row_count):
    for j in range(column_count):
        matrix_b[i][j] = float(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))


matrix_c = [[0.0]*column_count for _ in range(row_count)]

for i in range(row_count):
    for j in range(column_count):
        matrix_c[i][j] = matrix_a[i][j] * matrix_b[i][j]

v = [0.0] * column_count

for j in range(column_count):
    for i in range(row_count):
        v[j] += matrix_c[i][j]


print('Матрица A:')
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
        tmp += f'{matrix_a[i][j]:^6.3g}|'
    print(tmp)
print('-' * width)

print('Матрица B:')
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
        tmp += f'{matrix_b[i][j]:^6.3g}|'
    print(tmp)
print('-' * width)

print('Матрица C:')
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
        tmp += f'{matrix_c[i][j]:^6.3g}|'
    print(tmp)
print('-' * width)

print('Массив V:')
for j in range(column_count):
    print(f'{j + 1}-й элемент массива v: {v[j]:.3g}')
