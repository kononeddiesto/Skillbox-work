import datetime
import time
from typing import Callable


def logged(time_format, name, method):
    def wrapper(*args, **kwargs):
        full_time = datetime.datetime.today()
        date2 = ['%' + i if i.isalpha() else i for i in time_format]
        new_date = ''.join(date2)
        full_time.strftime(new_date)
        start = time.time()
        print("Запускается '{}.{}'. Дата и время запуска: {}".format(
            name,
            method.__name__,
            full_time))
        method_start = method(*args, **kwargs)
        print("Завершается '{}.{}', время работы = {}s".format(
            name,
            method.__name__,
            time.time() - start))
        with open('log.txt', 'a') as log_file:
            log_file.write('{} {} {}\n'.format(full_time, name, method))
            return method_start

    return wrapper


def log_methods(time_format: str) -> Callable:
    """
    Декоратор. Логгирует все методы класса, используя функцию logged.
    :param time_format: формат даты и времени (str)
    """

    def decorator(cls):
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            cur_method = getattr(cls, i_method)
            if hasattr(cur_method, '__call__'):
                decorated_a = logged(time_format, cls.__name__ + ".", cur_method)
                setattr(cls, i_method, decorated_a)
        return cls

    return decorator


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
