def search_coin(a, b, r):
    if (a - 0) ** 2 + (b - 0) ** 2 <= r ** 2:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
x = float(input('X:'))
y = float(input('Y:'))
radius = int(input('Введите радиус:'))

search_coin(x, y, radius)
