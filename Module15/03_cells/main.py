number_of_cells = int(input('Кол-во клеток:'))
cells = []
index_cells = []

for i in range(number_of_cells):
    print('Эффективность', i + 1, 'клетки:', end='')
    cell = int(input())
    if cell < i + 1:
        cells.append(cell)
        index_cells.append(i + 1)
print('Неподходящие значения: ', cells, index_cells)
