rollers_list = []
size_list = []
count = 0

number_of_skates = int(input('\nКол-во роликов: '))
for i_roller in range(number_of_skates):
    print('Размер', i_roller + 1, 'пары:', end=' ')
    size = int(input())
    rollers_list.append(size)

number_of_people = int(input('\nКол-во людей: '))
for i_size in range(number_of_people):
    print('Размер ноги', i_size + 1, 'человека:', end=' ')
    p_size = int(input())
    size_list.append(p_size)

for i in rollers_list:
    for num in range(len(size_list)):
        if i >= size_list[num]:
            count += 1
            size_list.remove(i)
            break
        else:
            continue

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count)
