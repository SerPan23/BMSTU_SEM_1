# Паншин Сергей ИУ-13Б
# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
# срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
# индексов начинается с 1).

x = int(input('Введите x матрицы: '))
y = int(input('Введите y матрицы: '))
z = int(input('Введите z матрицы: '))

while x <= 0 or y <= 0 or z <= 0:
    print('Ошибка x, y, и z должены быть больше 0')
    x = int(input('Введите x матрицы: '))
    y = int(input('Введите y матрицы: '))
    z = int(input('Введите z матрицы: '))

matrix = [[[0]*x for _ in range(y)] for _ in range(z)]

for i in range(z):
    for j in range(y):
        for k in range(x):
            matrix[i][j][k] = \
                int(input(f'Введите элемент с z = {i+1} и y = {j+1}: и x = {k+1}: '))

ind = int(input('Введите индекс среза матрицы: '))
while 0 < ind <= y:
    print('Индекс среза матрицы должен быть от 1 до y')
    ind = int(input('Введите индекс среза матрицы: '))

for i in range(z):
        for k in range(x):
            print(f'Элемент с z = {i + 1} и y = {ind}: и x = {k + 1}: {matrix[i][ind-1][k]}')