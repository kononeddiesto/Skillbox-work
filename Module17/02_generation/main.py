num = int(input('Введите число: '))

num_list = [1 if i % 2 == 0 else i % 5 for i in range(num)]

print('Результат: ', num_list)
