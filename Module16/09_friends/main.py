friends = int(input('Кол-во друзей: '))
debt = int(input('Долговых расписок: '))
ious = [[0, 0]]
for _ in range(friends - 1):
    ious.append([0, 0])

for i_debt in range(debt):
    print(i_debt + 1, 'расписка')
    who = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how = int(input('Сколько: '))
    ious[who - 1][0] += 1
    ious[who - 1][1] += how
    ious[from_whom - 1][0] -= 1
    ious[from_whom - 1][1] -= how


print('Баланс друзей: ')
for i in range(len(ious)):
    print(i + 1, ':', ious[i][1])
