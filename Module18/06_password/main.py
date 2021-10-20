while True:
    password = input('Придумайте пароль:')
    if len(password) > 8 and not password.islower() and not password.isalpha():
        num = [i for i in password if i.isdigit()]
        if len(num) >= 3:
            print('Это надёжный пароль!')
            break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        break
