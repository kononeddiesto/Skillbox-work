from itertools import combinations_with_replacement


if __name__ == '__main__':
    test = combinations_with_replacement(range(10), 4)
    for i in test:
        print(i)
