def function(any_tuple, element):
    if element in any_tuple:
        if any_tuple.count(element) > 1:
            first_index = any_tuple.index(element)
            second_index = any_tuple.index(element, first_index + 1) + 1
            return any_tuple[first_index:second_index]
        else:
            return any_tuple[any_tuple.index(element):]
    else:
        return ()


random_item = int(input('Введите элемент: '))
composite_tuple = (1, 6, 3, 4, 5, 6, 7)

print(function(composite_tuple, random_item))
