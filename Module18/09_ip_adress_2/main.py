while True:
    ip_address = input('Введите IP: ').split('.')
    if len(ip_address) < 4:
        print('Адрес - это четыре числа, разделенные точками')
        continue
    else:
        for i in ip_address:
            if not i.isdigit():
                print('{0} - не целое число'.format(i))
                break
            elif int(i) < 0:
                print('{0} не может быть меньше ноля'.format(i))
                break
            elif int(i) > 255:
                print('{0} превышает 255'.format(i))
                break
        else:
            print('IP-адрес корректен')
            break

