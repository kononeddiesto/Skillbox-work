zen_of_python = open('zen_of_python.txt', 'r')
zen_list = []
for i_line in zen_of_python:
    zen_list.append(i_line[:-1:])
for i_print in zen_list[::-1]:
    print(i_print)
zen_of_python.close()
