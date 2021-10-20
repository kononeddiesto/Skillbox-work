from random import randint


class Person:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 60
        self.house = house

    def act(self):
        num = randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.fridge < 10:
            self.go_to_mar()
        elif self.house.money < 50:
            self.work()
        elif num == 1:
            self.work()
        elif num == 2:
            self.eat()
        else:
            self.play()
        print()

    def eat(self):
        print('{} принимает пищу.'.format(self.name))
        self.satiety += 15
        self.house.fridge -= 15

    def work(self):
        print('{} зарабатывает деньги.'.format(self.name))
        self.satiety -= 15
        self.house.money += 10

    def play(self):
        print('{} играет!'.format(self.name))
        self.satiety -= 10

    def go_to_mar(self):
        print('{} пошел в магазин за продуктами.'.format(self.name))
        self.house.fridge += 10
        self.house.money -= 10


class House:

    def __init__(self):
        self.fridge = 50
        self.money = 0


my_house = House()
person_1 = Person('John', my_house)
person_2 = Person('Vika', my_house)
person_list = [person_1, person_2]

count = 0
while person_1.satiety > 0 or person_2.satiety > 0:
    for i_day in person_list:
        i_day.act()
    count += 1
    print('Прошел {} день'.format(count))
else:
    print('Человек умер :(')
