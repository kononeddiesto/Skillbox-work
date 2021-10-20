orders = int(input('Введите кол-во заказов: '))

all_order = dict()

for i in range(1, orders + 1):
    print('{0} заказ: '.format(i), end='')
    order = input().split()
    if order[0] not in all_order:
        all_order[order[0]] = dict()
    if order[0] in all_order:
        if order[1] in all_order[order[0]]:
            num = all_order[order[0]].pop(order[1])
            all_order[order[0]][order[1]] = int(order[2]) + int(num)
        else:
            all_order[order[0]][order[1]] = order[2]

for name in all_order:
    print('{0}:'.format(name))
    for i_pizza, i_number in all_order[name].items():
        print('\t{0}: {1}'.format(i_pizza, i_number))
    print()
