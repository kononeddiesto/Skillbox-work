def reverse_num(x):
    whole = int(x)
    whole_2 = 0
    fractional_2 = 0
    fractional = (x - (int(x))) * 100
    while whole > 0:
        digit = whole % 10
        whole //= 10
        whole_2 *= 10
        whole_2 += digit
    while fractional > 0:
        digit_2 = fractional % 10
        fractional //= 10
        fractional_2 *= 10
        fractional_2 += digit_2
    fractional_2 = round(fractional_2 / 100, 2)
    return whole_2 + fractional_2


n = float(input('Введите первое число: '))
k = float(input('Введите второе число: '))

print('Первое число наоборот: ', reverse_num(n))
print('Второе число наоборот: ', reverse_num(k))
print('Сумма: ', reverse_num(n) + reverse_num(k))
