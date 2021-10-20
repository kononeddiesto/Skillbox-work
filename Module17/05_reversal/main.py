def search_h(elem):
    result = 0
    for i in elem:
        if i != 'h':
            result += 1
        else:
            result += 1
            break
    return result


text = input('Введите строку: ')
start = search_h(text)
end = search_h(text[::-1])

print('Результат: ', text[:start] + text[-end - 1:start - 1:-1] + text[-end:])
