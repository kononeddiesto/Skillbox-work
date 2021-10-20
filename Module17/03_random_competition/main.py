import random

f_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
s_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

winner = [(f_team[x] if f_team[x] > s_team[x] else s_team[x]) for x in range(20)]

print('Первая команда: ', f_team)
print('Вторая команда: ', s_team)
print('Победители тура: ', winner)
