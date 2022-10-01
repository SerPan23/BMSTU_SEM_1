# Паншин Сергей ИУ7-13Б
# Вводятся координаты точки в трёхмерном пространстве.
# Определить в какой части бабочки или вне её находится проекция точки.


x, y, z = map(float, input('Введите координаты точки: ').split())

# переменные ниже координаты у при заданном х функций задающих рисунок

# левое верхнее крыло
upper_left_wing_1 = -1/8 * (x+9)**2 + 8
upper_left_wing_2 = 7*(x+8)**2 + 1
upper_left_wing_3 = 1/49 * (x+1)**2

# правое верхнее крыло
upper_right_wing_1 = -1/8 * (x-9)**2 + 8
upper_right_wing_2 = 7*(x-8)**2 + 1
upper_right_wing_3 = 1/49 * (x-1)**2

# правое нижнее крыло
lower_right_wing_1 = -3/35 * x**2 + 1/5 * x - 4/35
lower_right_wing_2 = 1/3 * x**2 - 10/3 * x + 4/3
lower_right_wing_3 = -2 * x**2 + 4*x - 4

# левое нижнее крыло
lower_left_wing_1 = -3/35 * x**2 - 1/5 * x - 4/35
lower_left_wing_2 = 1/3 * x**2 + 10/3 * x + 4/3
lower_left_wing_3 = -2 * x**2 - 4*x - 4

# тело
body_1 = 4 * x**2 - 6
body_2 = -4 * x**2 + 2

# усы
antennae = abs(3/2 * x) + 2


if upper_left_wing_2 <= y <= upper_left_wing_1 and y >= upper_left_wing_3:
    print('Точка лежит в верхнем левом крыле бабочки')
elif upper_right_wing_1 >= y >= upper_right_wing_3 and y >= upper_right_wing_2:
    print('Точка лежит в верхнем правом крыле бабочки')
elif lower_left_wing_1 >= y >= lower_left_wing_3 and y >= lower_left_wing_3:
    print('Точка лежит в нижнем левом крыле бабочки')
elif lower_right_wing_1 >= y >= lower_right_wing_2 and y >= lower_right_wing_3:
    print('Точка лежит в нижнем правом крыле бабочки')
elif body_2 >= y >= body_1:
    print('Точка лежит в теле бабочки')
elif y == antennae:
    print('Точка лежит на усах')
else:
    print('Точка лежит вне рисунка')
