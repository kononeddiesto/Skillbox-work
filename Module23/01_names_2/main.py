sym_count = 0
line_count = 0

with open('people.txt', 'r') as people_name:
    error_log = open('errors.log', 'w')
    try:
        for i_line in people_name:
            line_count += 1
            length = len(i_line)
            if i_line.endswith('\n'):
                length -= 1
                sym_count += length
            else:
                sym_count += len(i_line)
            try:
                if length < 3:
                    raise BaseException
            except BaseException:
                print('Длина {} строки меньше 3 символов'.format(line_count))
                error_log.write("BaseException('Длина {} строки меньше 3 символов'.format(line_count)")

    except FileNotFoundError:
        print('Файл не найден!')
        error_log.write("FileNotFoundError('Файл не найден!')")
    else:
        print('Код выполнен без ошибок!')
    finally:
        print('Всего символов: {}'.format(sym_count))
        print(error_log)
        error_log.close()
