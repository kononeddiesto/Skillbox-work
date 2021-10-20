import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        return x / y
    except ZeroDivisionError:
        print('Деление на ноль в первой функции!')


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        return y / x
    except ZeroDivisionError:
        print('Деление на ноль во второй функции!')


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            file_2 = open('result.txt', 'w')
            my_list = sorted([res1, res2, number])
        for i_answer in my_list:
            file_2.write(str(i_answer) + '\n')
except TypeError:
    print('Указанное значение при записи не строка!')
except FileNotFoundError:
    print('Файл не найден!')
else:
    print('Код выполнен без ошибок!')
finally:
    file_2.close()
