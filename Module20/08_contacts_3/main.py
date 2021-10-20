def add_contact():
    name = input('Введите Имя и Фамилия через пробел: ')
    number = int(input('Введите номер телефона: '))
    if name in phone_dict:
        print('Данный человек уже есть в телефонной книге.')
    else:
        phone_dict[name] = number
        print(phone_dict)


def search():
    surname = input('Введите фамилию: ')[:-1].capitalize()
    for i_name, i_num in phone_dict.items():
        if surname in i_name:
            print(i_name, i_num)


phone_dict = dict()

while True:
    act = input('Что необходимо сделать (добавить контакт/поиск человека по фамилии/end): ').lower()
    if act == 'добавить контакт':
        add_contact()
    elif act == 'поиск человека по фамилии':
        search()
    elif act == 'end':
        break
    else:
        print('Неверный ввод, повторите запрос.')
