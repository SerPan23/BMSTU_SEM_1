# Паншин Сергей ИУ7-13Б
# Написать программу для демонстрации работы метода сортировки
# (метод вставок с бинарным поиском) на примере массива целых чисел.
# Программа должна состоять из двух частей (этапов работы) и выполнять два действия
# последовательно:
# 1. сначала отсортировать заданный пользователем массив для доказательства
# корректности работы алгоритма
# 2. затем составить таблицу замеров времени сортировки списков трёх различных
# (заданных пользователем) размерностей и количества перестановок в каждом из них.
# В части 2 для каждой размерности списка необходимо исследовать:
# ● случайный список,
# ● отсортированный список,
# ● список, отсортированный в обратном порядке.

import time
import random


def binary_search(data, item, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if item == data[mid]:
            return mid + 1
        elif item > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


def insertion_sort(data, n):
    permutations = 0
    for i in range(n):
        j = i - 1
        selected = data[i]

        insert_loc = binary_search(data, selected, 0, j)

        while j >= insert_loc:
            data[j + 1] = data[j]
            permutations += 1
            j -= 1
        data[j + 1] = selected

    return permutations


def ordered_list_sort(n):
    data = [i for i in range(1, n + 1)]
    start_time = time.time()
    permutations = insertion_sort(data, n)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, permutations


def rev_ordered_list_sort(n):
    data = [i for i in range(n, 0, -1)]
    start_time = time.time()
    permutations = insertion_sort(data, n)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, permutations


def random_list_sort(n):
    data = [random.randint(-1000000, 10000000) for _ in range(n)]
    start_time = time.time()
    permutations = insertion_sort(data, n)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, permutations


def table_draw(data, table_widths):
    print('┌' + f'{"─" * table_widths[0]:^{table_widths[0]}}┬'
          + f'{"─" * table_widths[1]:^{table_widths[1]}}┬'
          + f'{"─" * table_widths[1]:^{table_widths[1]}}┬'
          + f'{"─" * table_widths[1]:^{table_widths[1]}}' + '┐')
    print(
        f'│{"":^{table_widths[0]}}│{"N1":^{table_widths[1]}}│{"N2":^{table_widths[1]}}│{"N3":^{table_widths[1]}}│')
    print(
        '│' + f'{"─" * table_widths[0]:^{table_widths[0]}}┼'
        + f'{"─" * table_widths[1]:^{table_widths[1]}}┼'
        + f'{"─" * table_widths[1]:^{table_widths[1]}}┼'
        + f'{"─" * table_widths[1]:^{table_widths[1]}}' + '│')
    print(f'│{"Тип списка":^{table_widths[0]}}│'
          + f'{"Время":^{table_widths[2] - 1}}│'
          + f'{"Перестановки":^{table_widths[2]}}│'
          + f'{"Время":^{table_widths[2] - 1}}│'
          + f'{"Перестановки":^{table_widths[2]}}│'
          + f'{"Время":^{table_widths[2] - 1}}│'
          + f'{"Перестановки":^{table_widths[2]}}│')
    row_count = len(data)
    for i in range(row_count):
        print(
            '│' + f'{"─" * table_widths[0]:^{table_widths[0]}}┼'
            + f'{"─" * table_widths[1]:^{table_widths[1]}}┼'
            + f'{"─" * table_widths[1]:^{table_widths[1]}}┼'
            + f'{"─" * table_widths[1]:^{table_widths[1]}}' + '│')
        print(f'│{data[i][0]:^{table_widths[0]}}│'
              + f'{data[i][1]:^{table_widths[2] - 1}.5g}│'
              + f'{data[i][2]:^{table_widths[2]}.5g}│'
              + f'{data[i][3]:^{table_widths[2] - 1}.5g}│'
              + f'{data[i][4]:^{table_widths[2]}.5g}│'
              + f'{data[i][5]:^{table_widths[2] - 1}.5g}│'
              + f'{data[i][6]:^{table_widths[2]}.5g}│')

    print(
        '└' + f'{"─" * table_widths[0]:^{table_widths[0]}}┴'
        + f'{"─" * table_widths[1]:^{table_widths[1]}}┴'
        + f'{"─" * table_widths[1]:^{table_widths[1]}}┴'
        + f'{"─" * table_widths[1]:^{table_widths[1]}}' + '┘')

n = None
while n is None:
    try:
        n = int(input('Введите размер массива: '))
        if n <= 0:
            n = None
            raise Exception()
    except Exception:
        print('Размер массива должен быть целым числом и больше 0')
mass = [0] * n
for i in range(n):
    tmp = None
    while tmp is None:
        try:
            tmp = int(input(f'Введите элемент {i+1}-й строки: '))
        except Exception:
            print('Элементом массива должно быть целым число')
    mass[i] = tmp

insertion_sort(mass, n)

for i in range(n):
    print(f'{i+1}-й элемент массива: {mass[i]}')
# print(*mass)

n1 = n2 = n3 = None
while n1 is None:
    try:
        n1 = int(input('Введите первый размер массива: '))
        if n1 <= 0:
            n1 = None
            raise Exception()
    except Exception:
        print('Размер массива должен быть целым числом и больше 0')
t1, k1 = ordered_list_sort(n1)
t4, k4 = random_list_sort(n1)
t7, k7 = rev_ordered_list_sort(n1)
while n2 is None:
    try:
        n2 = int(input('Введите второй размер массива: '))
        if n2 <= 0:
            n2 = None
            raise Exception()
    except Exception:
        print('Размер массива должен быть целым числом и больше 0')
t2, k2 = ordered_list_sort(n2)
t5, k5 = random_list_sort(n2)
t8, k8 = rev_ordered_list_sort(n2)
while n3 is None:
    try:
        n3 = int(input('Введите третий размер массива: '))
        if n3 <= 0:
            n3 = None
            raise Exception()
    except Exception:
        print('Размер массива должен быть целым числом и больше 0')
t3, k3 = ordered_list_sort(n3)
t6, k6 = random_list_sort(n3)
t9, k9 = rev_ordered_list_sort(n3)


table_data = [
    ['Упорядоченный', t1, k1, t2, k2, t3, k3],
    ['Случайный', t4, k4, t5, k5, t6, k6],
    ['Обратно упорядоченный', t7, k7, t8, k8, t9, k9]
]

table_draw(table_data, [25, 30, 15])
