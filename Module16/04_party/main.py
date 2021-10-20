guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    act = input('Гость пришел или ушел? ')
    if act == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    guest = input('Имя гостя: ')
    if act == 'пришел' or act == 'Пришел':
        if len(guests) < 6:
            print('Привет,', guest, '!')
            if guest in guests:
                print('Гость уже есть на вечеринке или тёзка!')
                guests.append(guest)
            else:
                guests.append(guest)
        else:
            print('Прости,', guest, ', но мест нет.')
            continue
    elif act == 'ушел' or act == 'Ушел':
        if guest in guests:
            print('Пока,', guest, '!')
            guests.remove(guest)
        else:
            print('Данного гостя и не было...')
    else:
        continue
    print()
