import math


class Car:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, x2, y2):
        self.dist = abs(math.sqrt((self.x - x2) ** 2 + (self.y - y2) ** 2))
        return print('Машина проехала расстояние ', round(self.dist, 1))

    def turn(self, new_angle):
        self.angle = new_angle


class Bus(Car):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.passengers = 0
        self.money = 0

    def move(self, x2, y2):
        self.dist = abs(math.sqrt((self.x - x2) ** 2 + (self.y - y2) ** 2))
        self.money += self.passengers * (self.dist * 0.1)
        return print('Автобус проехал расстояние {} км и провез {} пассажиров.\nЗаработал {} долларов'.format(
            round(self.dist, 1),
            self.passengers,
            round(self.money, 0)))

    def come_in(self, persons):
        if self.passengers < 100:
            self.passengers += persons
        else:
            self.passengers = self.passengers + (self.passengers - persons)
            print('Автобус полон!')

    def out_in(self, persons):
        self.passengers -= persons


car = Car(1, 2, 30)
bus = Bus(2, 3, 50)

bus.come_in(50)
print(bus.passengers)
bus.move(7, 8)
