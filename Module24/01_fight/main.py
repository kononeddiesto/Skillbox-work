import random


class Unit:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def fight(self, enemy):
        print('Атакует {}'.format(self.name))
        enemy.protection()
        print('У {} осталось {} здоровья. У {} осталось {} здоровья\n'.format(
            self.name, self.health, enemy.name, enemy.health
        ))

    def protection(self):
        defenced = random.randint(1, 2)
        if defenced == 1:
            print('Противник не смог защититься!')
            self.health -= 20
        else:
            print('Противник смог защититься.')


warrior_1 = Unit('Воин 1', 100)
warrior_2 = Unit('Воин 2', 100)

while warrior_1.health > 1 or warrior_2.health > 1:
    warrior_1.fight(warrior_2)
    warrior_2.fight(warrior_1)
    if warrior_1.health <= 1:
        print('Победу одержал Воин 2!')
        break
    elif warrior_2.health <= 1:
        print('Победу одержал Воин 1!')
        break
    else:
        continue