# Паншин Сергей ИУ7-13Б
# Поменять местами элементы последний нулевой и максимальный отрицательный

n = int(input('Введите количество элементов списка: '))

while n <= 0:
    print('Ошибка! Количество элементов должно быть больше 0')
    n = int(input('Введите количество элементов списка: '))

array = [0] * n

negative_nums = []
last_0_id = -1

for i in range(n):
    array[i] = int(input(f'Введите {i + 1} элемент списка: '))

    if array[i] < 0:
        negative_nums.append(array[i])

    if array[i] == 0:
        last_0_id = i

if last_0_id == -1:
    print('Ошибка! В данном массиве нет нулевых элементов')
elif len(negative_nums) == 0:
    print('Ошибка! В данном массиве нет отрицательных элементов')
else:
    max_negative_id = array.index(max(negative_nums))
    array[max_negative_id], array[last_0_id] = array[last_0_id], array[max_negative_id]
    for i in range(len(array)):
        print(f'{i + 1} элемент списка: {array[i]}')
