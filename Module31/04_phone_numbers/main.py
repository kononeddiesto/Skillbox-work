import re

if __name__ == '__main__':
    new_list = ['9999999999', '999999-999', '99999x9999', '8999999999', '8955565475']

    pattern = r'[89]\d{9}'
    for i_num, i_elem in enumerate(new_list):
        test = re.findall(pattern, i_elem)
        print('{} номер: {}'.format(i_num + 1, 'всё в порядке' if test else 'не подходит'))
