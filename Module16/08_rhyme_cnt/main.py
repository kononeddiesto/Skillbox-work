people = int(input('Кол-во человек: '))
num = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', num, ' человек')

players = list(range(1, people + 1))
play = 0

while len(players) > 1:
    print('Текущий круг людей:', players)
    if play + 1 <= len(players):
        play = play
    else:
        play = 0
    print('Начало счёта с номера ', players[play])
    for i in range(num - 1):
        if players[play] != players[-1]:
            play += 1
        elif players[play] == players[-1]:
            play = 0
    print('Выбывает человек под номером ', players[play])
    players.remove(players[play])


print('Остался человек под номером ', players[0])
