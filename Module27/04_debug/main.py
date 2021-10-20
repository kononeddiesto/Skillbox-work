import functools
from typing import Callable, Optional


def debug(func: Callable) -> Callable:
    """
    Декоратор, выводит название функции и её параметры
    перед выполнением функции.

    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Optional[str, int, None]:
        args = [*args]
        kwargs = {**kwargs}
        print('Вызывается {} {} {}'.format(func.__name__, args, kwargs))
        print("{} вернула значение '{}'".format(func.__name__, func(*args, **kwargs)))
        result = func(*args, **kwargs)
        print('{}\n'.format(result))

    return wrapped


@debug
def greeting(name: str, age: Optional[int, None] = None):
    """
    Функция приветствия.

    :param name:
    :param age:
    :return str:
    """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name,
                                                                            age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
