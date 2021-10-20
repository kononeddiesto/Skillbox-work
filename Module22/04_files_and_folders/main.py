import os


def all_catalog_file(cur_path, file_size=[], all_file=[], all_catalog=[]):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isfile(path):
            all_file.append(1)
            file_size.append(int(os.path.getsize(path)))
        elif os.path.isdir(path):
            all_catalog.append(1)
            all_catalog_file(path)
    return sum(file_size) / 1024, len(all_catalog), len(all_file)


new_path = input('Введите имя каталога через пробел: ')
catalog_path = os.path.abspath(new_path)
while not os.path.exists(catalog_path):
    new_path = os.path.join('..', new_path)
    catalog_path = os.path.abspath(new_path)

size, catalogs, files = all_catalog_file(catalog_path)
print('Размер каталога (в Кб): {}\nКоличество подкаталогов: {}\nКоличество файлов: {}'.format(
    size,
    catalogs,
    files))
