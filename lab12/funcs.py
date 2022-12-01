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
        return del_sentence_more_word_start_letter
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
    # text = [i.lstrip() for i in text]
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
            # print(word.split('-'))
            for i in word.split('-'):
                if not i.isalpha():
                    word = None
                    raise Exception()
        except Exception:
            print('Слово это набор букв без пробелов, цифр и других символов')
    for i in range(len(text)):
        tmp = text[i].split()
        for j in range(len(tmp)):
            if tmp[j] == word:
                tmp[j] = ''
            if tmp[j][:-1] == word and tmp[j][-1] in '.,?!:;':
                tmp[j] = tmp[j][-1]
        # while word in tmp:
        #     tmp.remove(word)
        text[i] = ' '.join(tmp)
    return text


# функция 5
def replace_all_word_occurrences(text):
    old_word = None
    while old_word is None:
        try:
            old_word = input('Введите слово которое хотите заменить: ')
            for i in old_word.split('-'):
                if not i.isalpha():
                    old_word = None
                    raise Exception()
        except Exception:
            print('Слово это набор букв без пробелов и цифр и других символов')

    new_word = None
    while new_word is None:
        try:
            new_word = input('Введите слово на которое хотите заменить: ')
            for i in new_word.split('-'):
                if not i.isalpha():
                    new_word = None
                    raise Exception()
        except Exception:
            print('Слово это набор букв без пробелов, цифр и других символов')
    for i in range(len(text)):
        tmp = text[i].split()
        j = -1
        try:
            while True:
                j = tmp.index(old_word, j + 1)
                tmp[j] = new_word
        except ValueError:
            pass
        text[i] = ' '.join(tmp)
    return text


# функция 6
def calculating_arithmetic_expression(text):
    for i in range(len(text)):
        cursor_pos = 0
        while cursor_pos < len(text[i]):
            if text[i][cursor_pos] in '*/':
                left_arg = ''
                min_k = cursor_pos
                for k in range(cursor_pos - 1, -1, -1):
                    if text[i][k] == ' ':
                        break

                    if text[i][k] == '-':
                        if not left_arg:
                            break
                        else:
                            left_arg = text[i][k] + left_arg
                            min_k = k
                            continue

                    if text[i][k] in '0123456789' and '-' not in left_arg:
                        left_arg = text[i][k] + left_arg
                    else:
                        break

                    min_k = k

                if not left_arg:
                    cursor_pos += 1
                    continue

                max_k = cursor_pos
                right_arg = ''
                for k in range(cursor_pos + 1, len(text[i])):
                    if text[i][k] == ' ':
                        break

                    if text[i][k] == '-':
                        if right_arg == '':
                            right_arg = text[i][k] + right_arg
                            max_k = k
                            continue

                    if text[i][k] in '0123456789':
                        right_arg += text[i][k]
                    else:
                        break

                    max_k += 1

                if not right_arg:
                    cursor_pos += 1
                    continue

                if text[i][cursor_pos] == '*':
                    result = str(int(left_arg) * int(right_arg))
                else:
                    try:
                        result = str(int(left_arg) // int(right_arg))
                    except:
                        print('Ошибка в тексте присутствует деление на ноль (Ответ заменен на None)!')
                        print('-' * 50)
                        result = 'None'

                text[i] = text[i][:min_k] + result + text[i][max_k + 1:]
                cursor_pos = min_k

            cursor_pos += 1

    return text


# функция 7
def del_sentence_more_word_start_letter(text):
    text = align_text_to_left(text)
    symbol = None
    while symbol is None:
        try:
            symbol = input('Введите символ начала слов: ')
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
                        try:
                            t_pos += 1
                            if len(text[t_str]) == t_pos:
                                t_str += 1
                                t_pos = 0
                            if text[t_str][t_pos] != '.' and text[t_str][t_pos] != ' ':
                                break
                        except:
                            break

                    sentences_pos.append([[t_str, t_pos], [i, tmp]])
                start_ind = tmp + 1

    need_sent_id = -1
    max_count = 0
    removable_sent = ''
    for i in range(len(sentences_pos)):
        tmp = ''
        if sentences_pos[i][1][0] == sentences_pos[i][0][0]:
            tmp = text[sentences_pos[i][1][0]][sentences_pos[i][0][1]:sentences_pos[i][1][1]]
        else:
            for j in range(sentences_pos[i][0][0], sentences_pos[i][1][0] + 1):
                if j == sentences_pos[i][1][0]:
                    tmp += ' ' + text[j][:sentences_pos[i][1][1] + 1] + ' '
                elif j == sentences_pos[i][0][0]:
                    tmp += ' ' + text[j][sentences_pos[i][0][1]:] + ' '
                else:
                    tmp += ' ' + text[j] + ' '
        # print(tmp, end='\n----------\n')
        tmp = tmp.split()
        tmp_count = 0
        for word in tmp:
            if word[0].lower() == symbol.lower():
                tmp_count += 1
        if need_sent_id == -1 and tmp_count > 0:
            need_sent_id = i
            max_count = tmp_count
            removable_sent = ' '.join(tmp)
        elif tmp_count > max_count:
            need_sent_id = i
            max_count = tmp_count
            removable_sent = ' '.join(tmp)
    if need_sent_id != -1:
        if sentences_pos[need_sent_id][0][0] == sentences_pos[need_sent_id][1][0]:
            text[sentences_pos[need_sent_id][0][0]] = \
                text[sentences_pos[need_sent_id][0][0]
                ][:sentences_pos[need_sent_id][0][1]] + \
                text[sentences_pos[need_sent_id][0][0]
                ][sentences_pos[need_sent_id][1][1] + 1:]

        else:
            text[sentences_pos[need_sent_id][0][0]] = \
                text[sentences_pos[need_sent_id][0]
                [0]][:sentences_pos[need_sent_id][0][1]]

            text[sentences_pos[need_sent_id][1][0]] = \
                text[sentences_pos[need_sent_id][1]
                [0]][sentences_pos[need_sent_id][1][1] + 1:]

            for k in range(sentences_pos[need_sent_id][1][0] - 1,
                           sentences_pos[need_sent_id][0][0], -1):
                text.pop(k)

    try:
        while text.index('') != -1:
            text.pop(text.index(''))
    except Exception:
        pass
    print('-' * 50)
    if removable_sent != '':
        print('Удаляемое предложение:')
        print(removable_sent)
    else:
        print('Такое предложение не найдено!')
    print('-' * 50)
    return align_text_to_left(text)


def print_text(text):
    if len(text) == 0:
        print('Вы удалили весь текст!')
        finish_program(text)
    else:
        print(*text, sep='\n')
