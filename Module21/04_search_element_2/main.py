site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, max_depth=None):
    if key in struct:
        return struct[key]
    elif not max_depth or max_depth > 1:
        if key in struct:
            return struct[key]
        if type(max_depth) == int:
            max_depth -= 1
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                if not max_depth:
                    result = find_key(sub_struct, key, max_depth)
                    if result:
                        break
                elif type(max_depth) == int and max_depth != 0:
                    result = find_key(sub_struct, key, max_depth)
                    if result:
                        break
                else:
                    result = None
                    break
        else:
            result = None
        return result


user_key = input('Какой ключ ищем? ')
depth = input('Глубина поиска? ')
if depth == '' or depth == '0':
    depth = None
else:
    depth = int(depth)
value = find_key(site, user_key, depth)
if value:
    print(value)
else:
    print('Такого ключа в структуре сайта нет!')
