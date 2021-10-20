class Parents:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.childs = []

    def info(self):
        all_children = [i_name.name for i_name in self.childs]
        print('Имя родителя {}, возраст родителя {}, список детей {}'.format(
            self.name, self.age, all_children
        ))

    def add_child(self, child):
        self.childs.append(child)

    def chek_child(self):
        print('{} проверяет детей.'.format(self.name))
        for i_child in self.childs:
            if i_child.tranquility == 1:
                print('\nРебенок {} {}'.format(i_child.name, i_child.state_tranquility[i_child.tranquility]))
                self.calm_down(i_child)
            elif i_child.hunger == 1:
                print('\nРебенок {} {}'.format(i_child.name, i_child.state_hunger[i_child.hunger]))
                self.feed(i_child)
            else:
                print('Дети спокойны и сыты.\n')

    def calm_down(self, child):
        child.tranquility = 0
        print('Родитель {} успокаивает ребенка {}.\n{} {}'.format(
            self.name, child.name, child.name, child.state_tranquility[child.tranquility]
        ))

    def feed(self, child):
        child.hunger = 0
        print('Родитель {} кормит ребенка {}.\n{} {}'.format(
            self.name, child.name, child.name, child.state_hunger[child.hunger]
        ))


class Child:
    state_tranquility = {0: 'Спокоен', 1: 'Кричит'}
    state_hunger = {0: 'Накормлен', 1: 'Голодный'}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tranquility = 0
        self.hunger = 0


child_1 = Child('Artur', 5)
child_2 = Child('Eva', 3)
parent_1 = Parents('Vova', 31)
parent_1.add_child(child_1)
parent_1.add_child(child_2)
child_1.hunger = 1
child_2.tranquility = 1
parent_1.chek_child()