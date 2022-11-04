# Паншин Сергей ИУ7-13Б
# числовая матрица удалить строки содержащие нулевые элементы

row_count = int(input('Введите количество строк: '))
column_count = int(input('Введите количество столбцов: '))

matrix = [[0] * column_count for _ in range(row_count)]         # наша матрица

for i in range(row_count):
    for j in range(column_count):
        matrix[i][j] = int(input(f'Введите элемент {i+1}-й строки и {j+1}-го столбца: '))

i = 0                               # счетчик цикла
count = 0                           # количество удаленных
while i < (row_count - count):
    if 0 in matrix[i]:
        matrix.pop(i)
        count += 1
    else:
        i += 1


if (row_count - count) > 0:
    tmp = f'{"":<3} '
    for j in range(column_count):
        tmp += f'{i:^6} '

    print(tmp)

    for i in range(row_count - count):
        tmp = f'{i+1:<3} '
        for j in range(column_count):
            tmp += f'{matrix[i][j]:^6} '
        print(tmp)
else:
    print('Матрица стала пустой')
