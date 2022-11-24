# Паншин Сергей ИУ7-13Б
# Быстрая сортировка

def quick_sort(data):
    data_len = len(data)
    if data_len == 1 or data_len == 0:
        return data

    left_data = quick_sort(data[: (data_len // 2)])
    right_data = quick_sort(data[(data_len // 2):])

    left_data_len = len(left_data)
    right_data_len = len(right_data)

    n = m = k = 0

    c = [0] * (left_data_len + right_data_len)

    while n < left_data_len and m < right_data_len:
        if left_data[n] < right_data[m]:
            c[k] = left_data[n]
            n += 1
        else:
            c[k] = right_data[m]
            m += 1
        k += 1

    while n < left_data_len:
        c[k] = left_data[n]
        n += 1
        k += 1

    while m < right_data_len:
        c[k] = right_data[m]
        m += 1
        k += 1

    for i in range(data_len):
        data[i] = c[i]

    return data


n = int(input('Введите размер массива: '))

a = [0] * n

for i in range(n):
    a[i] = int(input(f'Введите {i+1}-й элемент массива: '))

a = quick_sort(a)

for i in range(n):
    print(f'{i+1}-й элемент массива: {a[i]}')
