# Паншин Сергей ИУ7-13Б
# Программа для решения квадратных уравнений

a, b, c = map(float, input().split())

if a == 0:
    if b == 0:
        if c == 0:
            print('Бесконечно много решений')
        else:
            print('Нет решений')
    else:
        x = -c / b                                      # Нахождение корня
        print('x = {:.7g}'.format(x))
else:
    D = b**2 - 4 * a * c                                # Нахождение дискриминанта
    if D >= 0:
        if D == 0:
            x = -b / (2 * a)                            # Нахождение единственного корня
            print('x = {:.7g}'.format(x))
        else:
            x1 = (-b + D**0.5) / (2 * a)                # Нахождение первого корня
            x2 = (-b - D**0.5) / (2 * a)                # Нахождение второго корня
            print('x1 = {:.7g}'.format(x1))
            print('x2 = {:.7g}'.format(x2))
    else:
        print('Нет решений')
