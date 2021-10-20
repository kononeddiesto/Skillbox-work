my_list = [i for i in range(10)]
print(my_list)

new_list = []
for i in range(len(my_list) // 2):
    n = 1
    new_list.append((my_list[i * 2], my_list[i * 2 + n]))
    n += 1
print(new_list)

new_list_2 = list(tuple(my_list[i:i + 2]) for i in range(0, len(my_list), 2))
print(new_list_2)

new_list_3 = list(tuple(my_list[i:i + 2]) for i in my_list if i % 2 == 0)
print(new_list_3)
