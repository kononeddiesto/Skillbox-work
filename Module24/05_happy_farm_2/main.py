class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]
        self.matured = False

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            self.matured = True


class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden
        self.crop = []

    def care(self, garden):
        print('Садовник поливает картошку и окучивает грядку.')
        garden.grow_all()

    def harvest(self, crop_harv):
        if crop_harv.matured:
            self.crop.extend(crop_harv.potatoes)
            print('Садовник {} собирает урожай!'.format(self.name))
            crop_harv.potatoes.clear()
        else:
            print('Еще не все созрело, собирать рано!')


my_garden = PotatoGarden(5)
gardener = Gardener('John', my_garden)

for _ in range(3):
    gardener.care(my_garden)
    my_garden.are_all_ripe()
gardener.harvest(my_garden)
print(gardener.crop)
print(my_garden.potatoes)
