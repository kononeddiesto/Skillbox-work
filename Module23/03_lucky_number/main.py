import random


head_number = 0
with open('new_file.txt', 'w') as new_file:
    try:
        while head_number < 777:
            new_number = int(input('Введите число: '))
            head_number += new_number
            if random.randint(1, 13) == 3:
                raise BaseException
            else:
                new_file.write(str(new_number) + '\n')
    except FloatingPointError:
        print('Введено не целое число!')
    except BaseException:
        print('Ошибка вероятности!')
    else:
        print('Код выполнен без ошибок!')
