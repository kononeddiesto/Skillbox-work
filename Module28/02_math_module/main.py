import math
from typing import Union


class MyMath:
    @classmethod
    def circle_len(cls, radius: Union[int, float]) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: Union[int, float]) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_vol(cls, edge: Union[int, float]) -> Union[int, float]:
        return edge ** 3

    @classmethod
    def area_sphere(cls, radius: Union[int, float]) -> Union[int, float]:
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_vol(edge=2.2)
res_4 = MyMath.area_sphere(radius=6)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
