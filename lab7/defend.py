# Паншин Сергей ИУ7-13Б
# Найти строку наибольшой длины в которой непрерывное чередование букв и цифр

n = int(input('Введите количество элементов: '))

a = [' '] * n

for i in range(n):
    a[i] = input(f'Введите {i+1}-й элемент: ')

max_el = ''
flag = False

# eng_alp = 'qwertyuiopasdfghjklzxcvbnm'

for i in range(n):
    is_corr = False
    is_num_first = (a[i][0] in '0123456789')
    f = True
    for j in range(len(a[i])):
        # if a[i][j].lower() not in eng_alp and a[i][j] not in '0123456789':
        if not(97 <= ord(a[i][j].lower()) <= 122) and a[i][j] not in '0123456789':
            # print(ord(a[i][j].lower()), a[i][j].lower())
            f = False
            break
        if is_num_first:
            if (j % 2 != 0 and not(97 <= ord(a[i][j].lower()) <= 122)) or \
                    (j % 2 == 0 and a[i][j] not in '0123456789'):
                f = False
                break
        else:
            if (j % 2 == 0 and not(97 <= ord(a[i][j].lower()) <= 122)) or \
                    (j % 2 != 0 and a[i][j] not in '0123456789'):
                f = False
                break

    if f and len(a[i]) > len(max_el):
        max_el = a[i]
        flag = True

if flag:
    print(f'Наибольший элемент с заданными параметрами:')
    print(max_el)
else:
    print('Элемент с заданными параметрами не найден')


# print(ord('a'))
# print(ord('z'))