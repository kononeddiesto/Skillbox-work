def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 26] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


alphabet = ' abcdefghijklmnopqrstuvwxyz'

new_file = open('text.txt', 'w')
for _ in range(5):
    new_file.write('Hello\n')

new_file = open('text.txt', 'r')
text_file_read = new_file.read()
print('одержимое файла text.txt:\n{}'.format(text_file_read))

new_file = open('text.txt', 'r')
caesar_file = open('cipher_text.txt', 'a')
for i_index, i_line in enumerate(new_file):
    last_text = caesar_cipher(str(i_line[:-1]).lower(), i_index + 1)
    caesar_file.write('{}\n'.format(last_text))

new_file.close()
new_caesar_file = open('cipher_text.txt', 'r')
caesar_file_read = new_caesar_file.read()
print('Содержимое файла cipher_text.txt:\n{}'.format(caesar_file_read))
caesar_file.close()
