# Паншин Сергей ИУ7-13Б
# Найти наиболее длинную непрерывную последовательность
# возрастающих простых чисел

n = int(input('Введите количество элементов списка: '))

while n <= 0:
    print('Ошибка! Количество элементов должно быть больше 0')
    n = int(input('Введите количество элементов списка: '))

array = [0] * n

for i in range(n):
    array[i] = int(input(f'Введите {i + 1} элемент списка: '))

tmp = []
max_seq = []
f = True
for i in range(n):
    flag = True

    for j in range(2, array[i] // 2 + 1):
        if array[i] % j == 0:
            flag = False
            break

    if f and flag:
        f = False
        tmp.append(array[i])
    else:
        if array[i - 1] < array[i] and flag:
            tmp.append(array[i])
            if len(tmp) > len(max_seq):
                max_seq = tmp
        else:
            if flag:
                tmp = [array[i]]
            else:
                f = True
                tmp = []

if len(tmp) > len(max_seq):
    max_seq = tmp

if len(max_seq) == 0:
    print('Последовательность с данными критериями не найдена')
else:
    print(f'Длинна наиболее длинной последовательности: {len(max_seq)}')
    print('Элементы найденной последовательности:')
    for i in range(len(max_seq)):
        print(f'{i+1} элемент: {max_seq[i]}')
