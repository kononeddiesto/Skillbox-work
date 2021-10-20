from collections.abc import Iterable


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 90


def find_num(first_list: list, second_list: list, need_find: int) -> Iterable[int]:
    for x in first_list:
        for y in second_list:
            result = x * y
            yield result
            if result == need_find:
                print('Found!!!')
                print('Первое число {}, второе число {}, произведение {}, искомое число {}'.format(
                    x,
                    y,
                    result,
                    need_find))
                return


for index in find_num(list_1, list_2, to_find):
    print(index, end=' ')
