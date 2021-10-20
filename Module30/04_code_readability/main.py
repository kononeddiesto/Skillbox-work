if __name__ == '__main__':
    list_1 = []
    lst_1 = filter(lambda x: x % 2 != 0 and all(map(lambda i: x % i != 0, range(3, int(x ** 0.5) + 1, 2))) or x == 2,
                   range(2, 1001))
    print(list(lst_1))

    lst_2 = []
    for i in range(2, 1001):
        for j in lst_2:
            if i % j == 0:
                break
        else:
            lst_2.append(i)
    print(lst_2)
