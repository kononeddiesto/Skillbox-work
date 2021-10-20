import random

sticks = int(input('Кол-во палок: '))
throws = int(input('Кол-во бросков: '))

game = [i for i in range(1, 11)]
copy_game = game[:]

for i in range(throws):
    if len(copy_game) == 0:
        break
    print('Бросок', i + 1, end='. ')
    shoot = int(random.choice(copy_game))
    hit = int(random.randint(1, 4))
    if len(copy_game) < hit:
        hit = len(copy_game) - 1
    end = 0
    if shoot + hit > len(copy_game):
        end = copy_game[-1]
    else:
        end = copy_game[shoot - 1 + hit - 1]
    print('Сбиты палки с номера', shoot, '\nпо номер', end)
    for j in range(shoot, end + 1):
        if j in game:
            copy_game.remove(j)
            game.remove(j)
            game.insert(j - 1, 0)

result = ['.' if x == 0 else 'I' for x in game]
print('\nРезультат:', end=' ')
for i in result:
    print(i, end='')
