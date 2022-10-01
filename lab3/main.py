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
ab_coords_x = (xb - xa)
ab_coords_y = (yb - ya)
ac_coords_x = (xc - xa)
ac_coords_y = (yc - ya)
bc_coords_x = (xc - xb)
bc_coords_y = (yc - yb)

# длины векторов составляющих треугольник
len_ab = m.sqrt(ab_coords_x ** 2 + ab_coords_y ** 2)
len_ac = m.sqrt(ac_coords_x ** 2 + ac_coords_y ** 2)
len_bc = m.sqrt(bc_coords_x ** 2 + bc_coords_y ** 2)

p = (len_ab + len_ac + len_bc) / 2  # полупериметр треугольника
s = m.sqrt(p * (p - len_ab) * (p - len_ac) * (p - len_bc))  # площадь треугольника

if s == 0:
    print('Точки лежат на одной прямой, треугольник не существует')
else:
    # угла между векторами составляющих треугольник
    angle_a = m.cos((ab_coords_x * ac_coords_x + ab_coords_y * ac_coords_y) / (len_ab * len_ac))

    angle_b = m.cos((ab_coords_x * bc_coords_x + ab_coords_y * bc_coords_y) / (len_ab * len_bc))

    angle_c = m.cos((bc_coords_x * ac_coords_x + bc_coords_y * ac_coords_y) / (len_bc * len_ac))
    if angle_a >= angle_b:
        max_angle = angle_a
        side_by_max = len_bc
    else:
        max_angle = angle_b
        side_by_max = len_ac

    if angle_c > max_angle:
        max_angle = angle_c
        side_by_max = len_ab

    h = 2 * s / side_by_max  # высота из большого угла треугольника

    print('Длина первой стороны:          {:.7g}'.format(len_ab))
    print('Длина второй стороны:          {:.7g}'.format(len_bc))
    print('Длина третьей стороны:         {:.7g}'.format(len_ac))
    print('Длина высоты из большого угла: {:.7g}'.format(h))

    eps = m.e**-8

    if abs(len_ab - len_ac) <= eps or abs(len_ac - len_bc) <= eps or abs(len_bc - len_ab) <= eps:
        print('Заданный треугольник равнобедренный')
    else:
        print('Заданный треугольник не равнобедренный')

    x, y = map(int, input('Введите координаты точки: ').split())

    # векторные произведения
    dot_vec_comp_1 = (xa - x) * (yb - ya) - (ya - y) * (xb - xa)
    dot_vec_comp_2 = (xb - x) * (yc - yb) - (yb - y) * (xc - xb)
    dot_vec_comp_3 = (xc - x) * (ya - yc) - (yc - y) * (xa - xc)

    if dot_vec_comp_1 >= 0 and dot_vec_comp_2 >= 0 and dot_vec_comp_3 >= 0 \
            or dot_vec_comp_1 <= 0 and dot_vec_comp_2 <= 0 and dot_vec_comp_3 <= 0:
        a_dot_vec_coords_x = (x - xa)
        a_dot_vec_coords_y = (y - ya)
        b_dot_vec_coords_x = (x - xb)
        b_dot_vec_coords_y = (y - yb)
        c_dot_vec_coords_x = (x - xc)
        c_dot_vec_coords_y = (y - yc)
        distance_dot_ab = abs(ab_coords_x * a_dot_vec_coords_x
                              + ab_coords_y * a_dot_vec_coords_y) / len_ab

        distance_dot_bc = abs(bc_coords_x * b_dot_vec_coords_x
                              + bc_coords_y * b_dot_vec_coords_y) / len_bc

        distance_dot_ac = abs(ac_coords_x * c_dot_vec_coords_x
                              + ac_coords_y * c_dot_vec_coords_y) / len_ac
        min_distance = min(distance_dot_ab, distance_dot_bc, distance_dot_ac)
        if min_distance == 0:
            print('Точка находится на одной из сторон треугольника')
        else:
            print('Точка находится внутри треугольника, '
                  'растояние до ближайшей стороны '
                  'треугольника = {:.7g}'.format(min_distance))
    else:
        print('Точка не находится внутри треугольника')
