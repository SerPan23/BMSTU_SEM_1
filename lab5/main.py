# Паншин Сергей ИУ7-13Б
# Вариант 74

# Программа вычисляющая сумму бесконечного ряда с точностью
# до члена ряда ε

x = float(input('Введите значение аргумента: '))
eps = float(input('Введите точность: '))

while True:
    if eps <= 0:
        print('Ошибка! Эпсилон меньше либо равен нулю')
        eps = float(input('Введите точность: '))
    else:
        break

iter_count = int(input('Введите количество итераций: '))

while True:
    if iter_count <= 0:
        print('Ошибка! Количество итераций меньше либо равено нулю')
        iter_count = int(input('Введите количество итераций: '))
    else:
        break

step = int(input('Введите шаг: '))

while True:
    if step <= 0:
        print('Ошибка! Шаг меньше либо равен нулю')
        step = int(input('Введите шаг: '))
    elif step >= iter_count:
        print('Ошибка! Шаг больше либо равен количеству итераций')
        step = int(input('Введите шаг: '))
    else:
        break

current = 1

if abs(current) <= eps:
    print('Сумма бесконечного ряда - 0, вычислена за  1 итерацию.')
else:
    z = 0
    finish_i = -1
    table_width = 12 * 3 + 4
    print('-' * table_width)
    print(f'| {"№ итерации":^10} | {"t":^10} | {"s":^10} |')
    print('|' + '-' * (table_width - 2) + '|')
    for i in range(iter_count):

        numerator = 1
        for j in range(1, (2 * i - 1) + 1):
            numerator *= j

        denominator = 1
        for j in range(1, 2 * i + 1):
            denominator *= j

        current = (-1) ** i * (numerator / denominator) * x ** i

        z += current

        if i % step == 0:
            print(f'| {i + 1:^10.5g} | {current:^10.5g} | {z:^10.5g} |')

        if abs(current) <= eps:
            finish_i = i + 1
            break

    print('-' * table_width)

    if finish_i != -1:
        print(f'Сумма бесконечного ряда - {z:^.5g}, вычислена за {finish_i:^.5g} итерацию(й).')
    else:
        print('За указанное число итераций необходимой точности достичь не удалось.')
