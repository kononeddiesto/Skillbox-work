def palindrome(num_list):
    revers_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        revers_list.append(num_list[i_num])
    if num_list == revers_list:
        return True
    else:
        return False


nums = int(input('Кол-во чисел: '))
all_num = []
new_num = []
answer = []

for _ in range(nums):
    num = int(input('Число: '))
    all_num.append(num)

for i_nums in range(0, len(all_num)):
    for j_num in range(i_nums, len(all_num)):
        new_num.append(all_num[j_num])
    if palindrome(new_num):
        for i_answer in range(0, i_nums):
            answer.append(all_num[i_answer])
        answer.reverse()
        break
    new_num = []

print('Последовательность: ', all_num)
print('Нужно приписать чисел: ', len(answer))
print('Сами числа: ', answer)
