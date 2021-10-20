def score_key(a):
    return a[1][0] * 100000000 - a[1][1]


records = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')

column_players = dict()

for index in range(records):
    print('{0} запись: '.format(index + 1), end='')
    player = input().split(' ')
    if player[1] not in column_players:
        column_players[player[1]] = [(int(player[0])), (index + 1)]
    else:
        if int(player[0]) <= int(column_players[player[1]][0]):
            continue
        else:
            column_players[player[1]] = [(int(player[0])), (index + 1)]
players_list = list(column_players.items())
players_list.sort(key=score_key, reverse=True)

print('Итоги соревнований:')
sorted_dict = {k: v for k, v in players_list}
print('players_list', sorted_dict)

for i_winner in range(3):
    for i_player, i_score in sorted_dict.items():
        print('{0} место. {1} ({2})'.format(
            i_winner + 1, i_player, i_score[0])
        )
        sorted_dict.pop(i_player)
        break
