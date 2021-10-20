def shift(my_list, num_shift):
    new_list = my_list[-num_shift:] + my_list[:-num_shift]
    return new_list


list_of_numbers = []

for _ in range(5):
    num = int(input('Введите число: '))
    list_of_numbers.append(num)

numeral_shift = int(input('На какое количество сдвинуть ряд? '))

print('Изначальный список: ', list_of_numbers)
print('Сдвинутый список: ', shift(list_of_numbers, numeral_shift))
