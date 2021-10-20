violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

num_song = int(input('Сколько песен выбрать? '))
all_time_song = 0

for i_song in range(num_song):
    print('Название', i_song + 1, 'песни:', end=' ')
    new_song = input()
    for song in violator_songs:
        if new_song == song[0]:
            all_time_song += song[1]

print('Общее время звучания песен: ', round(all_time_song, 2), 'минут')
