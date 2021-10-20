import random


class House:
    living_List = []

    def __init__(self):
        self.count_money = 0
        self.eaten_food = 0
        self.bought_fur_coats = 0
        self.money = 100
        self.food = 50
        self.food_for_cat = 30
        self.mud = 0

    def __str__(self):
        return 'Денег в доме {}, еды для людей в доме {}, ' \
               'еды для животных в доме {}, грязи в доме {}'.format(
            self.money,
            self.food,
            self.food_for_cat,
            self.mud
        )

    def one_day(self):
        self.mud += 5
        if self.mud >= 90:
            self.living_List[0].happiness -= 10
            self.living_List[1].happiness -= 10

        for i_person in self.living_List:
            i_person.act()


class Husband(House):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.satiety = 30
        self.happiness = 100

    def __str__(self):
        return 'Сытость мужа {}, счастье мужа {}'.format(self.satiety, self.happiness)

    def act(self):
        if self.satiety <= 0:
            raise Exception('\tМуж умер от голода!')
        elif self.happiness < 10:
            raise Exception('\tМуж умер от депрессии!')
        elif self.happiness < 20:
            happy = [self.play(), self.pet_the_cat()]
            random.choice(happy)
        elif self.satiety < 30:
            self.eat()
        elif house.money < 50:
            self.go_to_work()

        else:
            self.go_to_work()

    def eat(self):
        self.satiety += 30
        house.food -= 30
        house.eaten_food += 30

    def play(self):
        self.satiety -= 10
        self.happiness += 20

    def go_to_work(self):
        self.satiety -= 10
        house.money += 150
        house.count_money += 150

    def pet_the_cat(self):
        self.satiety -= 10
        self.happiness += 5


class Wife(House):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.satiety = 30
        self.happiness = 100

    def __str__(self):
        return 'Сытость жены {}, счастье жены {}'.format(self.satiety, self.happiness)

    def act(self):
        if self.satiety <= 0:
            raise Exception('\tЖена умерла от голода!')
        elif self.happiness < 10:
            raise Exception('\t:Жена умерла от депрессии!')
        elif self.happiness < 20:
            happy2 = [self.buy_fur_coat(), self.pet_the_cat()]
            random.choice(happy2)
        elif self.satiety < 40:
            self.eat()
        elif house.mud > 80:
            self.clean_the_house()
        elif house.food < 60:
            self.buy_food()
        elif house.food_for_cat < 10:
            self.buy_food_for_cat()

    def eat(self):
        self.satiety += 30
        house.food -= 30
        house.eaten_food += 30

    def buy_food(self):
        self.satiety -= 10
        self.happiness -= 10
        house.money -= 60
        house.food += 60

    def buy_food_for_cat(self):
        self.satiety -= 10
        house.money -= 30
        house.food_for_cat += 30

    def buy_fur_coat(self):
        self.satiety -= 10
        if house.money > 350:
            house.money -= 350
            print('Купили жене шубу!')
            self.happiness += 60
            house.bought_fur_coats += 1
        else:
            self.pet_the_cat()

    def clean_the_house(self):
        self.satiety -= 10
        self.happiness -= 10
        if house.mud <= 100:
            house.mud -= house.mud

    def pet_the_cat(self):
        self.satiety -= 10
        self.happiness += 5


class Cat(House):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.satiety = 30

    def __str__(self):
        return 'Сытость кота {}'.format(self.satiety)

    def act(self):
        if self.satiety <= 0:
            raise Exception('\tКот умер от голода!')
        elif self.food_for_cat < 10:
            self.tear_wallpaper()
        elif self.satiety < 20:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        self.satiety += 20
        house.food_for_cat -= 10
        house.eaten_food += 10

    def sleep(self):
        self.satiety -= 10

    def tear_wallpaper(self):
        self.satiety -= 10
        house.mud += 5


house = House()
husband = Husband('Alex')
wife = Wife('Natasha')
cat = Cat('Igor')
house.living_List.append(husband)
house.living_List.append(wife)
house.living_List.append(cat)

for i_day in range(365):
    print('День {}\n'.format(i_day + 1))
    house.one_day()
    print(f'{house}\n{husband}\n{wife}\n{cat}\n')

print('Всего было: заработано денег {}, съедено еды {}, куплено шуб {}'.format(
    house.count_money,
    house.eaten_food,
    house.bought_fur_coats))
