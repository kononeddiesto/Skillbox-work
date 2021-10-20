nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def clear_list(some_list, new_list=[]):
    for index in some_list:
        if isinstance(index, list):
            clear_list(index)
        else:
            new_list.append(index)
    return new_list


print(clear_list(nice_list))
