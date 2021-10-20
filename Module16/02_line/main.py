first_class = []
second_class = []

for i_grow1 in range(160, 177, 2):
    first_class.append(i_grow1)

for i_grow2 in range(162, 181, 3):
    second_class.append(i_grow2)

first_class.extend(second_class)
for _ in range(len(first_class) - 1):
    for sort in range(len(first_class) - 1):
        if first_class[sort] > first_class[sort + 1]:
            first_class[sort], first_class[sort + 1] = first_class[sort + 1], first_class[sort]
print('Все ученики по росту: ', first_class)
