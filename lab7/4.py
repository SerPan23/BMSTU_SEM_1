# Паншин Сергей ИУ7-13Б
# Изменение элемента (замена всех заглавных гласных английских букв на
# строчные) в списке строк

n = int(input('Введите количество элементов списка: '))

while n <= 0:
    print('Ошибка! Количество элементов должно быть больше 0')
    n = int(input('Введите количество элементов списка: '))

a = [' '] * n                                       # наш список

for i in range(n):
    a[i] = input(f'Введите {i+1}-й элемент: ')

for i in range(n):
    tmp = ''                                        # хранение временной строки
    for j in range(len(a[i])):
        if 'A' <= a[i][j] <= 'Z':
            tmp += a[i][j].lower()
        else:
            tmp += a[i][j]
    a[i] = tmp


for i in range(n):
    print(f'{i+1}-й элемент: {a[i]}')
