from typing import List

if __name__ == '__main__':
    strings: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    results = map(lambda x, y: (x, y), strings, numbers)
    print(list(results))
