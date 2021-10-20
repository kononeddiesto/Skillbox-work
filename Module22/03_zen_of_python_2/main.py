zen_of_python = open('zen.txt', 'r')
letters, lines, words = 0, 0, 0
letters_dict = {}
for i_line in zen_of_python:
    lines += 1
    for i_word in i_line:
        if i_word.isalpha():
            letters += 1
            if i_word.lower() not in letters_dict:
                letters_dict[i_word.lower()] = 1
            else:
                letters_dict[i_word.lower()] += 1
        elif i_word == ' ':
            words += 1
zen_of_python.close()
print('Количество латинских букв {}\nКоличество строк {}\nКоличество слов {}'.format(letters, lines, words))
letter_list = (sorted(letters_dict.items()))
print('Буква встречающаяся в тексте меньшее количество раз:', sorted(letter_list, key=lambda x: x[-1])[0])
