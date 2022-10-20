# Паншин Сергей ИУ7-13Б
# Найти наиболее длинную непрерывную последовательность
# возрастающих простых чисел

n = int(input('Введите количество элементов списка: '))

while n <= 0:
    print('Ошибка! Количество элементов должно быть больше 0')
    n = int(input('Введите количество элементов списка: '))

array = [0] * n     # наш массив

for i in range(n):
    array[i] = int(input(f'Введите {i + 1} элемент списка: '))

# tmp = []            # временный массив
# max_seq = []        # максимальная последовательность
tmp_start = -1        # начало временной последовательности
tmp_end = -1          # конец временной последовательности

max_seq_start = -1    # начало максимальной последовательности
max_seq_end = -1      # конец максимальной последовательности

f = True            # флаг пустая ли временная последовательность
for i in range(n):
    flag = True     # флаг на простоту числа

    for j in range(2, array[i] // 2 + 1):
        if array[i] % j == 0:
            flag = False
            break

    if f and flag:
        f = False
        # tmp.append(array[i])
        tmp_start = i
    else:
        if array[i - 1] < array[i] and flag:
            # tmp.append(array[i])
            tmp_end = i
            if (tmp_end - tmp_start + 1) > (max_seq_end - max_seq_start + 1):
                max_seq_start, max_seq_end = tmp_start, tmp_end
        else:
            if flag:
                # tmp = [array[i]]
                tmp_start = i
            else:
                f = True
                # tmp = []
                tmp_start = tmp_end = -1

# if len(tmp) > len(max_seq):
#     max_seq = tmp
if (tmp_end - tmp_start + 1) > (max_seq_end - max_seq_start + 1):
    max_seq_start, max_seq_end = tmp_start, tmp_end

if (max_seq_end - max_seq_start + 1) == 0:
    print('Последовательность с данными критериями не найдена')
else:
    print(f'Длинна наиболее длинной последовательности: {(max_seq_end - max_seq_start + 1)}')
    print('Элементы найденной последовательности:')
    for i in range(max_seq_start, max_seq_end+1):
        print(f'{i+1} элемент: {array[i]}')
