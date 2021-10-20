my_list = []

for _ in range(5):
    x = int(input('Введите значения: '))
    my_list.append(x)

n = 1
while n < len(my_list):
    for i in range(len(my_list) - n):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    n += 1

print('Отсортированный список: ', my_list)
