import functools
from typing import Callable


def check_permission(user: str) -> Callable:
    def check(func) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if user in user_permissions:
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise PermissionError
            except PermissionError:
                print('{}: У пользователя недостаточно прав, чтобы выполнить функцию {}'.format(
                    PermissionError.__name__,
                    func.__name__))

        return wrapper

    return check


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
