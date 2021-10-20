text = input('Введите строку: ')
result = [i for i in text if i.isdigit()]

print('Цифры: {0}'.format(''.join(result)))
