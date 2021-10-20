num_file = open('numbers.txt', 'r')
print('Содержимое файла numbers.txt')
summ = 0
for i_line in num_file:
    print(i_line, end='')
    for i_digit in i_line:
        if i_digit == '\n':
            continue
        elif i_digit != ' ':
            summ += int(i_digit)
num_file.close()

answer_file = open('answer.txt', 'w')
answer_file.write(str(summ))
answer_file.close()

new_file = open('answer.txt', 'r')
print('\nСодержимое файла answer.txt')
answer = new_file.read()
print(answer)
new_file.close()
