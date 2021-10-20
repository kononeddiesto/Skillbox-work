import time
from typing import Callable


def decorator(func: Callable) -> Callable:
    """
    Декоратор, ожидание в 2 секунды

    :param func:
    :return:
    """
    def wrapped() -> None:
        start = time.time()
        time.sleep(2)
        result = func()
        end = time.time()
        timing = round(end - start, 4)
        print('Время выполнения функции: {} секунд(ы) '.format(timing))
        print(result)

    return wrapped


@decorator
def function() -> str:
    return 'Код функции!'


function()
