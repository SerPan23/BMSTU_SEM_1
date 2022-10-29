# Паншин Сергей ИУ7-13Б
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю

n = int(input('Введите размер матрицы: '))

while n <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите размер матрицы: '))

matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))

max_el = matrix[0][n-1]
flag_max = False
for i in range(n):
    for j in range(i+1, n):
        if max_el < matrix[i][j]:
            flag_max = True
            max_el = matrix[i][j]

min_el = matrix[n-1][n-1]
flag_min = False
for i in range(n):
    for j in range(i):
        if min_el > matrix[i][n-1-j]:
            flag_min = True
            min_el = matrix[i][n-1-j]

if flag_min and flag_max:
    print(f'Максимальное значение над главной диагональю = {max_el}')
    print(f'Минимальное значение под побочной диагональю = {min_el}')
else:
    print('Значения не найдены')
