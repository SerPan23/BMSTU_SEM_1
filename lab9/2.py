# Паншин Сергей ИУ-13Б
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
# вводить. Транспонирование не применять.

n = int(input('Введите размер матрицы: '))

while n <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите размер матрицы: '))

matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(f'Введите элемент с номером строки = {i+1} и номером столбца = {j+1}: '))



print('Исходная матрица')
tmp = f'{"i/j":^4}|'
for j in range(n):
    tmp += f'{j+1:^6}|'
width = len(tmp)
print('-' * width)
print(tmp)
print('-' * width)
for i in range(n):
    tmp = f'{i+1:^4}|'
    for j in range(n):
        tmp += f'{matrix[i][j]:^6}|'
    print(tmp)
print('-' * width)



for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = \
            matrix[j][i], matrix[i][j]

for j in range(n // 2):
    for i in range(n):
        matrix[i][j], matrix[i][n - 1 - j] = \
            matrix[i][n - 1 - j], matrix[i][j]

print('Промежуточная матрица')
tmp = f'{"i/j":^4}|'
for j in range(n):
    tmp += f'{j+1:^6}|'
width = len(tmp)
print('-' * width)
print(tmp)
print('-' * width)
for i in range(n):
    tmp = f'{i+1:^4}|'
    for j in range(n):
        tmp += f'{matrix[i][j]:^6}|'
    print(tmp)
print('-' * width)


for j in range(n // 2):
    for i in range(n):
        matrix[i][j], matrix[i][n - 1 - j] = \
            matrix[i][n - 1 - j], matrix[i][j]

for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = \
            matrix[j][i], matrix[i][j]

print('Итоговая матрица')
tmp = f'{"i/j":^4}|'
for j in range(n):
    tmp += f'{j+1:^6}|'
width = len(tmp)
print('-' * width)
print(tmp)
print('-' * width)
for i in range(n):
    tmp = f'{i+1:^4}|'
    for j in range(n):
        tmp += f'{matrix[i][j]:^6}|'
    print(tmp)
print('-' * width)