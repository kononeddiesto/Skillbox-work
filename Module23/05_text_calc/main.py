try:
    with open('calc.txt', 'r') as calc_math:
        for i_line in calc_math:
            try:
                math_ex = i_line[:-1]
                print(eval(math_ex))
            except SyntaxError:
                print('Синтаксическая ошибка! Нет оператора операции или данной операции не существует.')
except FileNotFoundError:
    print('Файл не найден!')
else:
    print('Код выполнен без ошибок!')
