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
    permutaions = 0
    for i in range(n):
        j = i - 1
        selected = data[i]

        loc = binary_search(data, selected, 0, j)

        while j >= loc:
            data[j + 1] = data[j]
            permutaions += 1
            j -= 1
        data[j + 1] = selected

    return permutaions


def ordered_list_sort(n):
    data = [i for i in range(1, n + 1)]
    start_time = time.time()
    permutaions = insertion_sort(data, n)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, permutaions


def rev_ordered_list_sort(n):
    data = [i for i in range(n, 0, -1)]
    start_time = time.time()
    permutaions = insertion_sort(data, n)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, permutaions


def random_list_sort(n):
    data = [random.randint(-1000000, 10000000) for _ in range(n)]
    start_time = time.time()
    permutaions = insertion_sort(data, n)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, permutaions


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


n = int(input('Введите размер массива: '))
mass = [0.0] * n
for i in range(n):
    mass[i] = float(input(f'Введите элемент {i+1}-й строки: '))

insertion_sort(mass, n)

print(*mass)

n1 = int(input('Введите первый размер массива: '))
t1, k1 = ordered_list_sort(n1)
t4, k4 = random_list_sort(n1)
t7, k7 = rev_ordered_list_sort(n1)
n2 = int(input('Введите второй размер массива: '))
t2, k2 = ordered_list_sort(n2)
t5, k5 = random_list_sort(n2)
t8, k8 = rev_ordered_list_sort(n2)
n3 = int(input('Введите третий размер массива: '))
t3, k3 = ordered_list_sort(n3)
t6, k6 = random_list_sort(n3)
t9, k9 = rev_ordered_list_sort(n3)


table_data = [
    ['Упорядоченный', t1, k1, t2, k2, t3, k3],
    ['Случайный', t4, k4, t5, k5, t6, k6],
    ['Обратно упорядоченный', t7, k7, t8, k8, t9, k9]
]

table_draw(table_data, [25, 30, 15])
