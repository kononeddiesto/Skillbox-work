text = input('Введите слово: ')
unique_letters = []

for i in list(text):
    if i in unique_letters:
        continue
    else:
        unique_letters.append(i)

print('Кол-во уникальных букв: ', len(unique_letters))
