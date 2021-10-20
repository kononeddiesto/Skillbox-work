from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, спрашивающий как дела.

    :param func:
    :return:
    """

    def wrapped(*args, ** kwargs) -> str:
        print('Как дела?', end=' ')
        input('')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, ** kwargs)
        return result

    return wrapped


@how_are_you
def test(argument_1, argument_2) -> Any:

    print('<Тут что-то происходит...{} {}>'.format(argument_1, argument_2))


test('Tom', 12)
