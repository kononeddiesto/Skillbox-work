import random

num_list = [random.randint(0, 3) for _ in range(10)]
print(num_list)
for num in num_list:
    if num == 0:
        num_list.append(num)
        num_list.remove(num)

print(num_list)
new_list = [i for i in num_list if i > 0]
print(new_list)
