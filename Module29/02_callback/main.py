import functools
from typing import Callable


def callback(route: str) -> Callable:
    """ Декоратор обратного вызова """

    def wrapper(func: Callable) -> Callable:
        app[route] = func

        @functools.wraps(func)
        def wrapped():
            ret = func()
            return ret

        return wrapped

    return wrapper


app = {}


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
