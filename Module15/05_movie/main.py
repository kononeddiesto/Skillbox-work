films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorite_movies_list = []

for i in range(len(films)):
    print('Введите фильм: ', end='')
    search_film = input()
    if search_film == 'end':
        break
    for film in films:
        if search_film == film:
            favorite_movies_list.append(search_film)
            break
        elif film == films[-1] and search_film != favorite_movies_list:
            print('Ошибка! Данного фильма нет в фильмотеке или Вы ввели неверное название фильма.')
        else:
            continue

print('Список любимых фильмов: ', favorite_movies_list)
