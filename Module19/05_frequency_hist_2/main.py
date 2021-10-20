def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input('Введите текст: ')
hist = histogram(text)

numerals = dict()
for num in range(len(hist)):
    new_list = list()
    for i, j in hist.items():
        if num == j:
            new_list.append(i)
    if new_list:
        numerals[num] = new_list

for key, value in numerals.items():
    print(key, ":", value)
