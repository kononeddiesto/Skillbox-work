def summa(x):
    summ = 0
    while x > 0:
        summ += x % 10
        x //= 10
    return summ


def number_of_digits(x):
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count


num = int(input('Введите число: '))

print('Сумма чисел:', summa(num))
print('Кол-во цифр в числе: ', number_of_digits(num))
print('Разность суммы и кол-ва цифр: ', summa(num) - number_of_digits(num))
