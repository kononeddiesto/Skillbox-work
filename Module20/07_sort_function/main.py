def sort(some_tuple):
    for i_int in some_tuple:
        if type(i_int) != int:
            return some_tuple
        elif type(i_int) == int and i_int == some_tuple[-1]:
            new_tuple = sorted(list(some_tuple))
            return tuple(new_tuple)


my_tuple = (4, 3, 2, 1)
print(sort(my_tuple))
