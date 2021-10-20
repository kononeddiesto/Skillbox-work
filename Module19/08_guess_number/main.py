import random

max_num = int(input('Введите максимальное число: '))
num = int(random.randint(1, max_num))

answer = set()
while answer != 'Помогите!':
    first_answer = input('Нужное число есть среди вот этих чисел?: ')
    if first_answer == 'Помогите!':
        print('Артём мог загадать следующие числа: {0}'.format(answer.difference(first_answer)))
        break
    first_answer = list(first_answer.split())
    if str(num) in first_answer and len(first_answer) == 1:
        print('Все верно, число {0}'.format(first_answer))
        break
    elif str(num) in first_answer:
        print('Ответ Артёма: Да')
        first_answer = set(first_answer)
        answer = first_answer.difference(answer)
    else:
        print('Ответ Артёма: Нет')
        answer = answer.difference(first_answer)
