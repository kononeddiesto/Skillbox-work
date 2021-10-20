violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

time_song = 0
number_of_songs = int(input('Сколько песен выбрать? '))
for i_num in range(number_of_songs):
    print('Название {0} песни: '.format(i_num + 1), end='')
    song = input()
    time_song += violator_songs[song]

print('Общее время звучания песен: {} минут'.format(round(time_song, 2)))
