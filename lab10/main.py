# Паншин Сергей ИУ7-13Б
# Написать программу для вычисления приближённого значения интеграла
# известной функции двумя разными методами:
# 1) Метод срединных прямоугольников
# 2) Метод парабол
# Далее на основе известной, заданной в программе, первообразной определить, какой
# метод является наиболее точным. Для этого требуется вычислить и отобразить
# абсолютную и относительную погрешности каждого из четырёх измерений. Метод,
# измерение которого с одним из разбиений дало самое близкое к первообразной
# значение, считается наиболее точным.
# Затем для другого, менее точного метода, итерационно вычислить количество участков
# разбиения, для которого интеграл будет вычислен с заданной точностью

import math as m


def F(x: float):
    return x ** 3 + 3 * x + 1


def f(x: float):
    return 3 * x ** 2 + 3


def middle_rectangles_method(a: float, b: float, n: int, func) -> float:
    h = (b - a) / n
    s = 0
    x = a + h / 2
    for i in range(1, n + 1):
        s += func(x)
        x += h
    integral = h * s
    return integral


def parabola_method(a: float, b: float, n: int, func) -> float:
    h = (b - a) / n
    s = 0
    x0 = a
    x1 = a + h
    for i in range(1, n + 1):
        s += func(x0) + 4 * func(x0 + h / 2) + func(x1)
        x0 += h
        x1 += h
    integral = s * h / 6
    return integral


start = end = n1 = n2 = None
while start is None or end is None:
    try:
        start, end = map(float, input("Введите начало и конец отрезка интегрирования: ").split())
        if start >= end:
            start = end = None
            raise Exception()
    except Exception:
        print('Началом и концом отрезка интегрирования могут быть только вещественные числа' +
              ' и начало должно быть строго меньше чем конец!' +
              '\nПовторите попытку ввода:')
while n1 is None or n2 is None:
    try:
        n1, n2 = map(int, input("Введите n1 и n2 (количества участков разбиения): ").split())
        if n1 <= 0 or n2 <= 0:
            n1 = n2 = None
            raise Exception()
    except Exception:
        print('Количества участков разбиения (n1 и n2) могут быть только целые числа больше 0!' +
              '\nПовторите попытку ввода:')


first_integral_N1 = middle_rectangles_method(start, end, n1, f)
first_integral_N2 = middle_rectangles_method(start, end, n2, f)

second_integral_N1 = parabola_method(start, end, n1, f)
second_integral_N2 = parabola_method(start, end, n2, f)

table_width = 49
print('-' * table_width)
print(f'{"":14} | {"N1":^14} | {"N2":^14}|')
print('-' * table_width)
print(f'{"Cр. прямоуг.":^14} | {first_integral_N1:^14.5g} | {first_integral_N2:^14.5g}|')
print('-' * table_width)
print(f'{"Парабол":^14} | {second_integral_N1:^14.5g} | {second_integral_N2:^14.5g}|')
print('-' * table_width)

true_integral = F(end) - F(start)
# print(f'True integral: {true_integral:.5g}')

delta_first_N1 = abs(true_integral - first_integral_N1)
delta_first_N2 = abs(true_integral - first_integral_N2)

delta_second_N1 = abs(true_integral - second_integral_N1)
delta_second_N2 = abs(true_integral - second_integral_N2)

deltas = [delta_first_N1, delta_first_N2, delta_second_N1, delta_second_N2]

deltas.sort()

if deltas[0] == delta_first_N1 or deltas[0] == delta_first_N2:
    worst_method = parabola_method
    msg = 'метод парабол'
else:
    worst_method = middle_rectangles_method
    msg = 'метод срединных прямоугольников'

print(f'Менее точный метод это {msg}')
print('Вычислим количество участков разбиения, для которого интеграл будет вычислен с заданной точностью')
eps = None
while eps is None:
    try:
        eps = float(input("Введите точность вычислений = "))
    except Exception:
        print('Точностью вычислений может быть только вещественное число' +
              '\nПовторите попытку ввода:')
n = 1
integral_1 = worst_method(start, end, n, f)
integral_2 = worst_method(start, end, 2 * n, f)
n *= 2
while abs(integral_1 - integral_2) > eps:
    n *= 2
    integral_2, integral_1 = integral_1, integral_2
    integral_2 = worst_method(start, end, n, f)

print(f'Количество участков разбиения = {n}')
