# Паншин Сергей ИУ7-13Б
# Добавить элемент в заданное место списка (по индексу) алгоритмически.

n = int(input('Введите количество элементов списка: '))

while n <= 0:
    print('Ошибка! Количество элементов должно быть больше 0')
    n = int(input('Введите количество элементов списка: '))

array = [0] * n

for i in range(n):
    array[i] = int(input(f'Введите {i + 1} элемент списка: '))

new_el = int(input('Введите элемент, который хотите добавить: '))
pos = int(input('Введите индекс(отсчет с 0) куда добавить новый элемент: '))

while not(0 <= pos <= n):
    print('Ошибка! Индекс должнен быть в пределах размера массива')
    pos = int(input('Введите индекс(отсчет с 0) куда добавить новый элемент: '))


array.append(0)

for i in range(n-1, pos-1, -1):
    array[i+1] = array[i]

array[pos] = new_el


for i in range(len(array)):
    print(f'{i + 1} элемент списка: {array[i]}')
