import datetime
from typing import Callable


def decorator_logging(func: Callable) -> Callable:
    def wrapped() -> None:
        print('Функция: {} \nДокументация к функции: {}'.format(func.__name__, func.__doc__))
        try:
            result = func()
            print(result)
        except (Exception, TypeError, SyntaxError, UnboundLocalError) as ex:
            with open('function_errors.log', 'a', encoding='utf-8') as logging:
                time = datetime.datetime.now()
                logging.write('Время: {}. Название функции: {}. Ошибка: {}.\n'.format(
                    time, func.__name__, ex))

    return wrapped


@decorator_logging
def test():
    """
    Функция test
    :return:
    """
    g = 1 + 'aer'
    print('Test!' + g)


@decorator_logging
def test2():
    """
    Функция test2
    :return:
    """
    print('Test2!')


@decorator_logging
def test3():
    """
    Функция test3
    :return:
    """
    pronto
    print('Test3!')


test()
test2()
test3()
