# Паншин Сергей ИУ7-13Б
# Выполнить транспонирование квадратной матрицы

n = int(input('Введите размер матрицы: '))

while n <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите размер матрицы: '))

matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))

# matrix = zip(*matrix)
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


tmp = f'{"":<3} '
for j in range(n):
    tmp += f'{j+1:^6}'
print(tmp)
for i in range(n):
    tmp = f'{i+1:<3} '
    for j in range(n):
        tmp += f'{matrix[i][j]:^6}'
    print(tmp)
