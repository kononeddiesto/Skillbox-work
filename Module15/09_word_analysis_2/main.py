text = input('Введите слово: ')

n = 0

new_list = list(text)
while n < len(new_list) // 2:
    if new_list[0 + n] == new_list[-1 - n]:
        n += 1
        if n == len(new_list) // 2:
            print('Слово является палиндромом')
            break
        continue
    elif new_list[0 + n] != new_list[-1 - n]:
        print('Слово не является палиндромом')
        break
