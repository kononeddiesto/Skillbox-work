text = input('Введите текст: ').split()
length = 0
line = ''

for i_word in text:
    if length < len(i_word):
        length = len(i_word)
        line = i_word

print('Самое длинное слово в строке: "{0}", его длина {1}'.format(line, length))
