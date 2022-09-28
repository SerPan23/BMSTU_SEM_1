# Паншин Сергей ИУ7-13Б

# Программа, которая по введенным целочисленным
# координатам трех точек на плоскости вычисляет длины сторон
# образованного треугольника и длину высоты, проведенной из
# наибольшего угла.
# И определяет, является ли треугольник равнобедренным.
#
# Далее вводятся координаты точки. Определяется, находится ли
# точка внутри треугольника. Если да, то находится расстояние
# от точки до ближайшей стороны треугольника.

import math as m

xa, ya = map(int, input('Введите координаты первой точки: ').split())
xb, yb = map(int, input('Введите координаты второй точки: ').split())
xc, yc = map(int, input('Введите координаты третьей точки: ').split())

# координаты векторов составляющих треугольник
ab_coords = [(xb - xa), (yb - ya)]
ac_coords = [(xc - xa), (yc - ya)]
bc_coords = [(xc - xb), (yc - yb)]

# длины векторов составляющих треугольник
len_ab = m.sqrt(ab_coords[0] ** 2 + ab_coords[1] ** 2)
len_ac = m.sqrt(ac_coords[0] ** 2 + ac_coords[1] ** 2)
len_bc = m.sqrt(bc_coords[0] ** 2 + bc_coords[1] ** 2)

# угла между векторами составляющих треугольник
angle_a = (ab_coords[0] * ac_coords[0] + ab_coords[1] * ac_coords[1]) / (len_ab * len_ac)

angle_b = (ab_coords[0] * bc_coords[0] + ab_coords[1] * bc_coords[1]) / (len_ab * len_bc)

angle_c = (bc_coords[0] * ac_coords[0] + bc_coords[1] * ac_coords[1]) / (len_bc * len_ac)

p = (len_ab + len_ac + len_bc) / 2                          # полупериметр треугольника
s = m.sqrt(p * (p - len_ab) * (p - len_ac) * (p - len_bc))  # площадь треугольника

if angle_a >= angle_b:
    max_angle = angle_a
    side_by_max = len_bc
else:
    max_angle = angle_b
    side_by_max = len_ac

if angle_c > max_angle:
    max_angle = angle_c
    side_by_max = len_ab

h = 2 * s / side_by_max   # высота из большого угла треугольника

print('Длина первой стороны:          {:.7g}'.format(len_ab))
print('Длина второй стороны:          {:.7g}'.format(len_bc))
print('Длина третьей стороны:         {:.7g}'.format(len_ac))
print('Длина высоты из большого угла: {:.7g}'.format(h))


if len_ab == len_ac or len_ac == len_bc or len_bc == len_ab:
    print('Заданный треугольник равнобедренный')
else:
    print('Заданный треугольник не равнобедренный')

x, y = map(int, input('Введите координаты точки: ').split())

# векторные произведения
dot_vec_comp_1 = (xa - x)*(yb - ya) - (ya - y)*(xb - xa)
dot_vec_comp_2 = (xb - x)*(yc - yb) - (yb - y)*(xc - xb)
dot_vec_comp_3 = (xc - x)*(ya - yc) - (yc - y)*(xa - xc)


if dot_vec_comp_1 >= 0 and dot_vec_comp_2 >= 0 and dot_vec_comp_3 >= 0 \
        or dot_vec_comp_1 <= 0 and dot_vec_comp_2 <= 0 and dot_vec_comp_3 <= 0:
    a_dot_vec_coords = [(x - xa), (y - ya)]
    b_dot_vec_coords = [(x - xb), (y - yb)]
    c_dot_vec_coords = [(x - xc), (y - yc)]
    distance_dot_ab = abs(ab_coords[0] * a_dot_vec_coords[0]
                          + ab_coords[1] * a_dot_vec_coords[1]) / len_ab

    distance_dot_bc = abs(bc_coords[0] * b_dot_vec_coords[0]
                          + bc_coords[1] * b_dot_vec_coords[1]) / len_bc

    distance_dot_ac = abs(ac_coords[0] * c_dot_vec_coords[0]
                          + ac_coords[1] * c_dot_vec_coords[1]) / len_ac
    print('Точка находится внутри треугольника, '
          'растояние до ближайшей стороны '
          'треугольника = {:.7g}'.format(min(distance_dot_ab,
                                             distance_dot_bc,
                                             distance_dot_ac)))
else:
    print('Точка не находится внутри треугольника')
