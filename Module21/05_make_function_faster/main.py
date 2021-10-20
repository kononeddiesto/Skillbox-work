import math


def calculating_math_func(num, data={}):
    if data:
        return data[3]
    else:
        data[1] = math.factorial(num)
        data[2] = data[1] / num ** 3
        data[3] = data[2] ** 10
        return data[3]


print(calculating_math_func(5))
