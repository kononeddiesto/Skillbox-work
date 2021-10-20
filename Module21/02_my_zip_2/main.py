def zip2(first_str, second_tuple):
    min_str = min(len(first_str), len(second_tuple))
    my_tuple_pairs = [(string[index], some_tuple[index]) for index in range(min_str)]
    return my_tuple_pairs


string = input('Строка: ')
some_tuple = [i for i in range(4)]

print(zip2(string, some_tuple))
