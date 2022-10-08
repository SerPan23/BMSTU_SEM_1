# Паншин Сергей ИУ7-13Б
# Вариант 74

# Программа вычисляющая сумму бесконечного ряда с точностью
# до члена ряда ε

x = float(input('Введите значение аргумента: '))
eps = float(input('Введите точность: '))
iter_count = int(input('Введите количество итераций: '))
step = int(input('Введите шаг: '))

z = 0
finish_i = -1
table_width = 12*3+4
print('-' * table_width)
print(f'| {"№ итерации":^10} | {"t":^10} | {"s":^10} |')
print('|' + '-' * (table_width-2) + '|')
for i in range(iter_count):

    numerator = 1
    for j in range(1, (2 * i - 1) + 1):
        numerator *= j

    denominator = 1
    for j in range(1, 2 * i + 1):
        denominator *= j

    current = (-1)**i * (numerator/denominator) * x**i

    z += current

    if abs(current) <= eps:
        finish_i = i+1
        break

    if i % step == 0:
        print(f'| {i+1:^10.5g} | {current:^10.5g} | {z:^10.5g} |')

print('-' * table_width)

if finish_i != -1:
    print(f'Сумма бесконечного ряда - {z:^.5g}, вычислена за {finish_i:^.5g} итераций.')
else:
    print('За указанное число итераций необходимой точности достичь не удалось.')
