numbers_of_country = int(input('Кол-во стран: '))
i_country = dict()
for i_num in range(1, numbers_of_country + 1):
    print('{0} страна: '.format(i_num), end='')
    country = input().split()
    i_country[country[0]] = country[1:]

for i_city in range(3):
    print('{0} город: '.format(i_city + 1), end='')
    city = input()
    for j in i_country.keys():
        if city in i_country.get(j):
            search_country = j
            print('Город {0} расположен в стране {1}.'.format(city, search_country))
            break
        elif city not in j:
            continue
    else:
        print('По городу {0} данных нет.'.format(city))
