import os


def gen_files_path(find_file, directory):
    for i_elem in os.listdir(directory):
        if find_file in os.listdir(directory):
            return print('Нашли файл!\n', os.path.join(directory, find_file))
        if os.path.isfile(os.path.join(directory, i_elem)):
            file_path = os.path.join(directory, i_elem)
            print('Файл, путь: ', end='')
            yield file_path
        elif os.path.isdir(os.path.join(directory, i_elem)):
            dir_path = os.path.join(directory, i_elem)
            print('Каталог, путь: ', end='')
            yield dir_path
            for index in gen_files_path(find_file, dir_path):
                yield index


name_file = input('Введите имя каталога: ')
path = os.path.abspath(os.path.sep)
for elem in gen_files_path(name_file, path):
    print(elem)
