first_years = int(input('Введите первый год:'))
second_years = int(input('Введите второй год:'))

print('Года от ', first_years, 'до', second_years, 'с тремя одинаковыми цифрами:')

while first_years < second_years:
    for i in range(10):
        if 3 == str(first_years).count(str(i)):
            print(first_years)
    first_years += 1

# По-другому не выходит
