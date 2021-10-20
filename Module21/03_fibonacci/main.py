def fibonacci(num):
    result = 1
    if num > 2:
        result = fibonacci(num - 1) + fibonacci(num - 2)
    return result


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число: {}'.format(fibonacci(num_pos)))
