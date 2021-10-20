def min_delitel(num):
    min_delit = 0
    for delit in range(2, num + 1):
        if num % delit == 0:
            if min_delit == 0:
                min_delit = delit
            elif min_delit < delit:
                continue
            else:
                min_delit = delit
        else:
            continue
    return min_delit


x = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы: ', min_delitel(x))
