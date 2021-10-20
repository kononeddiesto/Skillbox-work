from collections.abc import Iterable

num = int(input('Введите число: '))


class Iterator:
    def __init__(self, sym: int) -> None:
        self.counter = 0
        self.sym = sym

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> Iterable[int]:
        if self.counter < self.sym:
            self.counter += 1
            return self.counter ** 2
        else:
            raise StopIteration


def num_gen(number: int) -> Iterable[int]:
    for i_num in range(1, number + 1):
        yield i_num ** 2
    else:
        return


result_3 = [index ** 2 for index in range(1, num + 1)]
