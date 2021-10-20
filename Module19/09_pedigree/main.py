num = int(input('Введите количество человек: '))

my_dict = dict()

for i_pare in range(num - 1):
    print('{0} пара: '.format(i_pare + 1), end='')
    names = input().split()
    if names[1] in my_dict:
        my_dict[names[0]] = my_dict[names[1]] + 1
    else:
        my_dict[names[1]] = 0
        my_dict[names[0]] = 1

print('“Высота” каждого члена семьи: ')
sort_list = list(my_dict.keys())
sort_list.sort()

for name in sort_list:
    print(name, my_dict[name])
