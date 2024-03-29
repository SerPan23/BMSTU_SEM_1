# Паншин Сергей ИУ7-13Б
# Вводятся координаты точки в трёхмерном пространстве.
# Определить в какой части бабочки или вне её находится проекция точки.


x, y = map(float, input('Введите координаты точки: ').split())

#

# тело
body_1 = 4 * x**2 - 6
body_2 = -4 * x**2 + 2

# плавник
up_side_fin = -2*x + 1
down_side_fin = 2*x - 5

# хвост
tail_up = -abs(x) - 6
tail_down = -8

# глаз
eye = (x - 0.3)**2 + (y + 0.2)**2


if eye <= 0.09:
    print('Точка лежит в глазу рыбки')
elif body_2 >= y >= body_1 and -1 <= x <= 1:
    print('Точка лежит в теле рыбки')
elif tail_up >= y >= tail_down and -2 <= x <= 2:
    print('Точка лежит в хвосте рыбки')
elif up_side_fin >= y >= down_side_fin and -0.809 <= x <= 1.5:
    print('Точка лежит в плавнике рыбки')
else:
    print('Точка лежит вне рисунка')
