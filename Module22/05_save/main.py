import os


def save(new_text):
    savekeep_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
    catalog_path = os.path.abspath(os.path.sep)
    for i_path in savekeep_path:
        catalog_path += os.path.join(i_path)
        catalog_path += os.path.join(os.path.sep)
    name_file = input('Введите имя файла: ')
    name_file = '{}{}.txt'.format(catalog_path, name_file)
    print(name_file)
    if os.path.exists(name_file):
        new_file = open(name_file, 'w')
        write_file = input('Вы действительно хотите перезаписать файл? да/нет ').lower()
        if write_file == 'да':
            new_file.write(new_text)
            print('Файл успешно перезаписан!')
        else:
            print('Отмена перезаписи!')
    else:
        new_file = open(name_file, 'w')
        new_file.write(new_text)
        print('Файл успешно сохранён!')
    new_file.close()


text = input('Введите строку: ')
save(text)

