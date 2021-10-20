def short(first_str, second_tuple):
    return min(len(first_str), len(second_tuple))


string = input('Строка: ')
some_tuple = [i for i in range(4)]

my_tuple_pairs = ((string[index], some_tuple[index]) for index in range(short(string, some_tuple)))
print(my_tuple_pairs)
for i_elem in my_tuple_pairs:
    print(i_elem)
