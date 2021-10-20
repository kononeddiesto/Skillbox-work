def add_log_good(name):
    with open('registrations_good.log', 'a') as my_logger:
        my_logger.write('{}\n'.format(name))


def add_log_bad(name_log, error):
    with open('registrations_bad.log', 'a') as log_bad:
        log_bad.write('{}: {}\n'.format(name_log, error))


def valid_str(user):
    try:
        if len(user) < 3:
            add_log_bad(user, IndexError, )
            raise IndexError
        if not user[0].isalpha():
            add_log_bad(user, NameError)
            raise NameError
        if '@' not in user[1] and '.' not in user[1]:
            add_log_bad(user, SyntaxError)
            raise SyntaxError
        if user[2].isdigit():
            if 10 < int(user[2]) > 99 or isinstance(user[2], float):
                add_log_bad(user, ValueError)
                raise ValueError
        add_log_good(user)
    except IndexError:
        pass
        # print('НЕ присутствуют все три поля!')
    except NameError:
        pass
        # print('Поле имени содержит НЕ только букв!')
    except SyntaxError:
        pass
        # print('Поле емейл НЕ содержит @ и/или .(точку)!')
    except ValueError:
        pass
        # print('Поле возраст НЕ является числом от 10 до 99!')


try:
    with open('registrations.txt', 'r', encoding='utf-8') as registration_file:
        for i_data in registration_file:
            user_data = i_data.split()
            valid_str(user_data)
except FileNotFoundError:
    add_log_bad('Файл не найден!', FileNotFoundError)
else:
    print('Код выполнен без ошибок.')
