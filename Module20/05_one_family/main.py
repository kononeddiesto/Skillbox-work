names = {'Сидоров Никита': 35,
         'Сидорова Алина': 34,
         'Сидоров Павел': 10,
         'Иванов Коля': 25,
         'Смирнова Оля': 28
         }

surname = input('Введите фамилию: ')[:-2].capitalize()

for i_name, i_age in names.items():
    if surname in i_name:
        print(i_name, i_age)
