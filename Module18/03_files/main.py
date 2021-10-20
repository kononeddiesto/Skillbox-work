name_file = input('Название файла: ')

if name_file.startswith(('@', '№', '$', '%', '^', '&', '*', '(', ')')):
    print('Ошибка: название начинается на один из специальных символов')
elif not name_file.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
