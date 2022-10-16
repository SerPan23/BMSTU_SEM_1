# Паншин Сергей ИУ7-13Б
# Найти значение K-го экстремума в списке

n = int(input('Введите количество элементов списка: '))

while n <= 0:
    print('Ошибка! Количество элементов должно быть больше 0')
    n = int(input('Введите количество элементов списка: '))

array = [0] * n

for i in range(n):
    array[i] = int(input(f'Введите {i + 1} элемент списка: '))

k = int(input('Введите номер экстремума: '))

count = 0

for i in range(1, n):
    if array[i - 1] > array[i] and array[i] < array[i + 1] \
            or array[i - 1] < array[i] and array[i] > array[i + 1]:
        count += 1

    if count == k:
        print(f'Значение K-го экстремума в списке: {array[i]}')
        break
else:
    print(f'Значение K-го экстремума в списке найти не удалось')
