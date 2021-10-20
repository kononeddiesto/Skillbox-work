def revers(word):
    reverse_word = word[-1::-1]
    return reverse_word


def symbol(next_word):
    new_text = ''
    new_text2 = ''
    for i in next_word:
        if i not in ".,:;!_*-+()/#¤%&)":
            new_text += i
        elif i in ".,:;!_*-+()/#¤%&)" and new_text.isalpha():
            new_text2 = revers(new_text)
            new_text2 += i
            new_text = ''
        elif i in ".,:;!_*-+()/#¤%&)":
            new_text += i
        elif i == next_word[-1] and i.isalpha():
            new_text2 += revers(new_text)
            return new_text2
        elif i == next_word[-1] and not i.isalpha():
            new_text2 += revers(new_text)
            new_text2 += i
            return new_text2
    new_text2 += revers(new_text)
    return new_text2


text = input('Сообщение: ').split()
result = ''

for index in text:
    if index.isalpha():
        result += revers(index) + ' '
    else:
        result += symbol(index) + ' '

print('Новое сообщение: {0}'.format(''.join(result)))
