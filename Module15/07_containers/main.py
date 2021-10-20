number_of_containers = int(input('Кол-во контейнеров: '))
count = 0
all_containers = []

for index in range(number_of_containers):
    print('Введите вес контейнера: ', end='')
    container = int(input())
    all_containers.append(container)

new_container = int(input('Введите вес нового контейнера: '))
for index_cont in all_containers:
    if new_container <= index_cont:
        count += 1
        continue
    else:
        count += 1
        print('Номер, куда встанет новый контейнер: ', count)
        break
