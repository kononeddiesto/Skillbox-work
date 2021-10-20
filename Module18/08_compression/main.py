text = input('Введите строку: ')
result = []
count = 0
num = 0

for i in text:
    if i == text[num - 1]:
        continue
    sym = i
    result.append(i)
    while text[0 + num] == sym:
        count += 1
        num += 1
        if num == len(text):
            result.append(str(count))
            break
    else:
        result.append(str(count))
        count = 0
        continue

print('Закодированная строка: {0}'.format(''.join(result)))
