import random


class LifeError:
    def __str__(self):
        return 'Ошибка!'


class KillError(LifeError):
    def __str__(self):
        return 'Убил!'


class DrunkError(LifeError):
    def __str__(self):
        return 'Запил!'


class CarCrashError(LifeError):
    def __str__(self):
        return 'Разбил машину!'


class GluttonyError(LifeError):
    def __str__(self):
        return 'Объелся!'


class DepressionError(LifeError):
    def __str__(self):
        return 'Депрессия!'


def one_day():
    num = random.randint(1, 10)
    if num == 3:
        error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
        print(error)
        with open('karma.log', 'a') as karma_log:
            karma_log.write(error.__name__ + '\n')
    else:
        return random.randint(1, 7)


carma = 0
while carma < 500:
    day = one_day()
    if isinstance(day, int):
        carma += day
        print('Всего кармы {}'.format(carma))
else:
    print('Достиг просвещения!')
