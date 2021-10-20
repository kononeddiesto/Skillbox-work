from typing import Callable, Any
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.

    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        res = func(*args, **kwargs)
        print('Функция {func} была вызвана: {count} раз(а)'.format(
            func=func.__name__, count=wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@counter
def test():
    print('Тест!')


test()
test()
test()
