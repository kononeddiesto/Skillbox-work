def enumerate(max_num):
    if max_num == 0:
        return 0
    enumerate(max_num - 1)
    return print(max_num, end=' ')


number = int(input('Введите число: '))
enumerate(number)
