# Паншин Сергей ИУ-13Б
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования.

row_count = int(input('Введите количество строк матрицы: '))
column_count = int(input('Введите количество столбцов матрицы: '))

while row_count <= 0 or column_count <= 0:
    print('Ошибка количество строк и столбцов должен быть больше 0')
    row_count = int(input('Введите количество строк матрицы: '))
    column_count = int(input('Введите количество столбцов матрицы: '))

matrix = [[' ']*column_count for _ in range(row_count)]

for i in range(row_count):
    for j in range(column_count):
        matrix[i][j] = input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: ')


print('Матрица до преобразований:')
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
        tmp += f'{matrix[i][j]:^6}|'
    print(tmp)
print('-' * width)

for i in range(row_count):
    for j in range(column_count):
        if matrix[i][j].lower() in 'aeiquy':
            matrix[i][j] = '.'


print('Матрица после преобразований:')
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
        tmp += f'{matrix[i][j]:^6}|'
    print(tmp)
print('-' * width)
