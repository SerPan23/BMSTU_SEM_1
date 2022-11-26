def function_select(number):
    if number == 1:
        return align_text_to_left
    elif number == 2:
        return align_text_to_right
    elif number == 3:
        return align_text_to_width
    elif number == 4:
        return deleting_all_word_occurrences
    elif number == 5:
        return replace_all_word_occurrences
    elif number == 6:
        return calculating_arithmetic_expression
    elif number == 7:
        return del_longer_sentence_start_letter
    elif number == 0:
        return finish_program


# функция 0
def finish_program(text):
    print('Программа завершена!')
    exit()


# функция 1
def align_text_to_left(text):
    for i in range(len(text)):
        tmp = text[i].split()
        text[i] = ' '.join(tmp)
    text = [i.lstrip() for i in text]
    return text


# функция 2
def align_text_to_right(text):
    for i in range(len(text)):
        tmp = text[i].split()
        text[i] = ' '.join(tmp)
    max_len = 0
    for i in text:
        if len(i) > max_len:
            max_len = len(i)
    for i in range(len(text)):
        l = len(text[i])
        text[i] = ' ' * (max_len - l) + text[i]

    return text


# функция 3
def align_text_to_width(text):
    max_len = 0
    for i in text:
        if len(i) > max_len:
            max_len = len(i)
    # print('max_len', max_len)
    for i in range(len(text)):
        tmp = text[i].split()
        tmp_len = len(''.join(tmp))
        missing_length = max_len - tmp_len
        space_count = len(tmp) - 1
        space_len = missing_length // space_count
        if missing_length % space_count == 0:
            spaces = ' ' * space_len
            text[i] = spaces.join(tmp)
        else:
            joined_tmp = ''
            need_add_count = missing_length - (space_count * space_len)
            for j in range(len(tmp)):
                joined_tmp += tmp[j]
                if j == len(tmp) - 1:
                    continue
                elif j >= len(tmp) - 1 - need_add_count:
                    joined_tmp += ' ' * (space_len + 1)
                else:
                    joined_tmp += ' ' * space_len
            text[i] = joined_tmp
            # print(i, len(text[i]), tmp_len, missing_length, space_count, space_len)
    return text


# функция 4
def deleting_all_word_occurrences(text):
    word = None
    while word is None:
        try:
            word = input('Введите слово которое хотите удалить: ')
            # print(word, word.isalpha())
            if not word.isalpha():
                word = None
                raise Exception()
        except Exception:
            print('Слово это набор букв без пробелов, цифр и других символов')
    for i in range(len(text)):
        tmp = text[i].split()
        while word in tmp:
            tmp.remove(word)
        text[i] = ' '.join(tmp)
    return text


# функция 5
def replace_all_word_occurrences(text):
    old_word = None
    while old_word is None:
        try:
            old_word = input('Введите слово которое хотите заменить: ')
            if not old_word.isalpha():
                old_word = None
                raise Exception()
        except Exception:
            print('Слово это набор букв без пробелов, цифр и других символов')

    new_word = None
    while new_word is None:
        try:
            new_word = input('Введите слово на которое хотите заменить: ')
            if not new_word.isalpha():
                new_word = None
                raise Exception()
        except Exception:
            print('Слово это набор букв без пробелов, цифр и других символов')
    for i in range(len(text)):
        tmp = text[i].split()
        i = -1
        try:
            while True:
                i = tmp.index(old_word, i + 1)
                tmp[i] = new_word
        except ValueError:
            pass
        text[i] = ' '.join(tmp)
    return text


# функция 6
def calculating_arithmetic_expression(text):
    text = align_text_to_left(text)
    text_in_str = ''.join(text)
    arithmetic_expression_pos = []
    start_ind = 0
    while True:
        tmp_mul = text_in_str.find('*', start_ind)
        if tmp_mul == -1:
            break
        else:
            arithmetic_expression_pos.append([tmp_mul])
            start_ind = tmp_mul + 1
    start_ind = 0
    while True:
        tmp_del = text_in_str.find('/', start_ind)
        if tmp_del == -1:
            break
        else:
            arithmetic_expression_pos.append([tmp_del])
            start_ind = tmp_del + 1

    arithmetic_expression_pos.sort()
    # print(arithmetic_expression_pos)
    for i in range(len(arithmetic_expression_pos)):
        start_ind = arithmetic_expression_pos[i][0]
        start_sub = -1
        while start_ind > 0:
            start_ind -= 1

            if text_in_str[start_ind].isnumeric():
                start_sub = start_ind
            elif text_in_str[start_ind] != ' ':
                break
        if start_sub == -1:
            continue
        end_ind = arithmetic_expression_pos[i][0]
        end_sub = -1
        while end_ind < len(text_in_str) - 1:
            end_ind += 1
            if text_in_str[end_ind].isnumeric():
                end_sub = end_ind
            elif text_in_str[end_ind] != ' ':
                break
        if end_sub == -1:
            continue

        arithmetic_expression_pos[i].append(start_sub)
        arithmetic_expression_pos[i].append(end_sub)

    results = []
    for i in arithmetic_expression_pos:
        if len(i) == 3:
            expression = text_in_str[i[1]:i[2]+1].split()
            expression = ''.join(expression)
            tmp = ''
            exp = []
            for j in expression:
                if j not in '*/':
                    tmp += j
                else:
                    exp.append(int(tmp))
                    tmp = ''
                    exp.append(j)
            if tmp.isnumeric():
                exp.append(int(tmp))

            if len(exp) % 3 == 0 and len(exp) >= 3:
                res = exp[0]
                for j in range(1, len(exp), 2):
                    if exp[j] == '*':
                        res *= exp[j+1]
                    elif exp[j] == '/':
                        res /= exp[j+1]

                results.append([i[1], i[2], res])

    results.sort(reverse=True)
    # print(results)
    for i in results:
        start_in_text = get_pos_in_text(text, i[0])
        end_in_text = get_pos_in_text(text, i[1])
        if start_in_text[0] == end_in_text[0]:
            text[start_in_text[0]] = text[start_in_text[0]][:start_in_text[1]] \
                                     + str(i[2]) + text[start_in_text[0]][end_in_text[1]+1:]
        else:
            text[start_in_text[0]] = text[start_in_text[0]][:start_in_text[0]] + str(i[2])
            for j in range(start_in_text[0] + 1, end_in_text[0] + 1):
                if j == end_in_text[0]:
                    text[j] = text[j][end_in_text[1]+1:]
                else:
                    text[j] = ''
    try:
        while text.index('') != -1:
            text.pop(text.index(''))
    except Exception:
        pass
    return align_text_to_left(text)


def get_pos_in_text(text, pos_in_str):
    str_ind = 0
    while pos_in_str > len(text[str_ind]):
        # print(pos_in_str, str_ind, len(text[str_ind]))
        pos_in_str -= len(text[str_ind])
        str_ind += 1

    ind = pos_in_str
    return str_ind, ind


# функция 7
def del_longer_sentence_start_letter(text):
    text = align_text_to_left(text)
    symbol = None
    while symbol is None:
        try:
            symbol = input('Введите символ начала предложения которое хотите удалить: ')
            if not symbol.isalpha() or len(symbol) > 1:
                symbol = None
                raise Exception()
        except Exception:
            print('Символ начала должен быть буквой')

    sentences_pos = []
    for i in range(len(text)):
        start_ind = 0
        while True:
            tmp = text[i].find('.', start_ind)
            if tmp == -1:
                break
            else:
                if len(sentences_pos) == 0:
                    sentences_pos.append([[0, 0], [i, tmp]])
                else:
                    t_str = sentences_pos[-1][1][0]
                    t_pos = sentences_pos[-1][1][1]
                    while True:
                        t_pos += 1
                        if len(text[t_str]) == t_pos:
                            text[t_str] += 1
                            t_pos = 0
                        if text[t_str][t_pos] != '.' and text[t_str][t_pos] != ' ':
                            break

                    sentences_pos.append([[t_str, t_pos], [i, tmp]])
                start_ind = tmp + 1

    # print(sentences_pos)
    max_len_id = -1
    for i in range(len(sentences_pos)):
        sent_len = 0
        if sentences_pos[i][1][0] == sentences_pos[i][0][0]:
            sent_len = sentences_pos[i][1][1] - sentences_pos[i][0][1]
        else:
            for j in range(sentences_pos[i][0][0], sentences_pos[i][1][0] + 1):
                if j == sentences_pos[i][1][0]:
                    sent_len += len(text[j]) - sentences_pos[i][1][1]
                elif j == sentences_pos[i][0][0]:
                    sent_len += len(text[j]) - sentences_pos[i][0][1]
                else:
                    sent_len += len(text[j])
        sentences_pos[i].append(sent_len)
        if text[sentences_pos[i][0][0]][sentences_pos[i][0][1]].lower() == symbol.lower():
            if max_len_id == -1:
                max_len_id = i
            elif sentences_pos[max_len_id][2] < sentences_pos[i][2]:
                max_len_id = i

    # print(sentences_pos)
    # print(max_len_id)
    for i in range(sentences_pos[max_len_id][0][0], sentences_pos[max_len_id][1][0] + 1):
        if sentences_pos[max_len_id][0][0] < i < sentences_pos[max_len_id][1][0]:
            text[i] = ''
        elif sentences_pos[max_len_id][0][0] == i:
            text[i] = text[i][:sentences_pos[max_len_id][0][1]]
        elif sentences_pos[max_len_id][1][0] == i:
            text[i] = text[i][sentences_pos[max_len_id][1][1] + 1:]
    try:
        while text.index('') != -1:
            text.pop(text.index(''))
    except Exception:
        pass
    return align_text_to_left(text)


def print_text(text):
    print(*text, sep='\n')
