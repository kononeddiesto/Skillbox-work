import math
from typing import Union


class Triangle:
    def __init__(self, base: Union[int, float], side: Union[int, float]) -> None:
        self.__base = base
        self.__side = side

    def __str__(self) -> str:
        return "Основание: {} Сторона: {}".format(self.__base, self.__side)

    @property
    def base(self) -> Union[int, float]:
        return self.__base

    @base.setter
    def base(self, base: Union[int, float]) -> None:
        self.__base = base

    @property
    def height(self) -> Union[int, float]:
        return self.__side

    @height.setter
    def height(self, side: Union[int, float]) -> None:
        self.__side = side

    def perimeter(self) -> Union[int, float]:
        return self.__base + self.__side + self.__side

    def area(self) -> Union[int, float]:
        return self.__base / 4 * math.sqrt(4 * self.__side ** 2 - self.__base ** 2)


class Square:
    def __init__(self, side: int) -> None:
        self.__side = side

    def __str__(self) -> str:
        return "Стороны: {}".format(self.__side)

    @property
    def side(self) -> Union[int, float]:
        return self.__side

    @side.setter
    def side(self, side: Union[int, float]) -> None:
        self.__side = side

    def perimeter(self) -> Union[int, float]:
        return self.__side * 4

    def area(self) -> Union[int, float]:
        return self.__side ** 2


class AreaMixin:
    @classmethod
    def all_area(cls, figure_list) -> Union[int, float]:
        result = 1
        for i_size in figure_list:
            if i_size.__class__ == Square:
                result += i_size.area()
            else:
                result += i_size.area()
        return result


class Pyramid(Triangle, AreaMixin):
    def __init__(self, base: Union[int, float], side: Union[int, float]) -> None:
        super().__init__(base, side)
        self.all_side = [Square(base),
                         Triangle(base, side),
                         Triangle(base, side),
                         Triangle(base, side),
                         Triangle(base, side)]


class Cube(Square, AreaMixin):
    def __init__(self, side: int) -> None:
        super().__init__(side)
        self.all_side = [Square(side) for _ in range(6)]


cube = Cube(5)
print(cube)
pyramid = Pyramid(10, 6)
print(pyramid)
print(cube.all_area(cube.all_side))
print(pyramid.all_area(pyramid.all_side))
