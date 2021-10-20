num = int(input('Введите количество пар слов: '))

new_dict = dict()
for index in range(1, num + 1):
    pair = input('{0} пара: '.format(index)).lower().split(' - ')
    new_dict[pair[0]] = pair[1]

while True:
    word = input('Введите слово: ').lower()
    if word == 'end':
        break
    for i, j in new_dict.items():
        if word == i:
            print('Синоним: {0}'.format(new_dict[i]).capitalize())
            break
        elif word == j:
            print('Синоним: {0}'.format(i).capitalize())
            break
    else:
        print('Такого слова в словаре нет.')
