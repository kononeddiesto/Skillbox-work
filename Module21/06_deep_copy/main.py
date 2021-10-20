site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def new_site(some_site, name):
    some_site['html']['head']['title'] = 'Куплю/продам {} недорого'.format(name)
    some_site['html']['body']['h2'] = 'У нас самая низкая цена на {}'.format(name)
    print_site(some_site)


def print_site(second_site, space=1):
    for i_key, i_value in second_site.items():
        if isinstance(i_value, dict):
            print(' ' * space, i_key)
            print_site(i_value, space + 3)
        else:
            print(' ' * space, i_key, ':', i_value)


number_of_site = int(input('Сколько сайтов: '))
site_list = []
for index in range(number_of_site):
    name_product = input('\nВведите название продукта для нового сайта:')
    site_list.append(name_product)
    for i_name in site_list:
        print('Сайт для {}: '.format(i_name))
        new_site(site, i_name)
