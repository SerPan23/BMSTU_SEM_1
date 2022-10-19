# Паншин Сергей ИУ7-13Б
import math as m

x = float(input('x: '))
eps = float(input('eps: '))

n = 1
a = 1
s = 0
while True:
    # a = (((-1) ** n) * (x ** n)) / m.factorial(n)
    a *= -1
    a *= x
    a /= n
    if abs(a) < eps:
        break
    s += a
    n += 1

print(f"Сумма ряда = {s}")
