first_list = []
second_list = []
new_list = []

for i_fir in range(3):
    num_fir = int(input('Введите число для первого списка: '))
    first_list.append(num_fir)
for i_sec in range(7):
    num_sec = int(input('Введите число для второго списка: '))
    second_list.append(num_sec)

first_list.extend(second_list)

for num in range(9):
    for sort in first_list:
        if first_list.count(num) > 1:
            first_list.remove(num)
        else:
            continue

print('Новый первый список с уникальными элементами:', first_list)
