first_group = open('first_tour.txt', 'r')
first_group_read = first_group.read()
print('Содержимое файла first_tour.txt:\n{}'.format(first_group_read))

first_group_read2 = open('first_tour.txt', 'r')
player_dict = {}
player_score = 0
for i_player in first_group_read2:
    if i_player[:-1].isdigit():
        player_score = int(i_player[:-1])
    else:
        new_player = i_player.split()
        player_dict[new_player[0] + ' ' + new_player[1]] = int(new_player[2])

winner_dict = {}
for i_winner, i_score in player_dict.items():
    if i_score > player_score:
        winner_dict[i_winner] = i_score
sort_winner_dict = sorted(winner_dict, key=lambda x: x[2], reverse=True)
new_sort_dict = {win_player: winner_dict[win_player] for win_player in sort_winner_dict}

second_group = open('second_tour.txt', 'w')
second_group.write('{}\n'.format(str(len(sort_winner_dict))))
count = 1
for i_sec_win, i_sec_sc in new_sort_dict.items():
    winner = i_sec_win.split()
    second_group.write('{}) {}. {} {}\n'.format(count, winner[1][:1], winner[0], i_sec_sc))
    count += 1

second_group = open('second_tour.txt', 'r')
second_group_read = second_group.read()
print('Содержимое файла second_tour.txt:\n{}'.format(second_group_read))
first_group.close()
second_group.close()
