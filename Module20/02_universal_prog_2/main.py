def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    for index in range(2, num):
        if num % index == 0:
            return False
        else:
            return True


def short_list(new_list):
    return list(j for i, j in enumerate(new_list) if is_prime(i))


my_list = {i: 1 for i in range(10)}

print(short_list(my_list))
