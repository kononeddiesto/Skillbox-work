y = input('По оси OY: ').lower()
x = input('По оси OX: ').lower()
x_way = 0
y_way = 0

for _ in range(2):
    if x.startswith('east'):
        x_way = int(x[-2:])
    elif x.startswith('west'):
        x_way = ('-' + x[-2:])
    if y.startswith('north'):
        y_way = int(y[-2:])
    elif y.startswith('south'):
        y_way = ('-' + y[-2:])

print('Координаты: {0} {1}'.format(x_way, y_way))
