text = input('Введите текст: ')

list_of_vowels = [i for i in text if i in 'уеаояию']

print('Список гласных букв: ', list_of_vowels)
print('Длина списка: ', len(list_of_vowels))
