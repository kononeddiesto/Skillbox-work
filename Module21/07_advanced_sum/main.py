def my_sum(num=None, *args):
    result = 0
    if isinstance(num, int):
        result += num
    else:
        for index in num:
            if isinstance(index, list):
                result += my_sum(index)
            elif type(index) == int:
                result += index
                continue
            if index == num[-1]:
                return result
    result += sum(args)
    return result


print('Ответ: {}'.format(my_sum([[1, 2, [3]], [1], 3])))

print('Ответ: {}'.format(my_sum(1, 2, 3, 4, 5)))
