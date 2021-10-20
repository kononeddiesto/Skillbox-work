from collections import Counter


if __name__ == '__main__':
    def can_be_poly(val: str) -> bool:
        return len(list(filter(lambda x: x % 2, Counter(val).values()))) <= 1


    print(can_be_poly('ababc'))
    print(can_be_poly('abbbc'))
