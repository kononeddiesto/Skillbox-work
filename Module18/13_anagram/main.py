first_word = list(input('Введите 1 слово:'))
second_word = input('Введите 2 слово:')

for i in second_word:
    if i in first_word:
        first_word.remove(i)

if not first_word:
    print('Слова являются анаграммами друг друга')
else:
    print('Слова не являются анаграммами друг друга')
