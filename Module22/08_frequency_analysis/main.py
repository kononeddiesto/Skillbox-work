text = open('text.txt', 'r').read().lower()
words_dict = {}
num = 0
for i_word in text:
    if ord('a') <= ord(i_word) <= ord('z'):
        get_word = words_dict.get(i_word, 0)
        words_dict[i_word] = get_word + 1
        num += 1
words_list = [(index, '{:.3f}'.format(words_dict[index] / num)) for index in words_dict.keys()]
words_list.sort(key=lambda x: x[0])
words_list.sort(key=lambda x: x[1], reverse=True)
string_answer = "\n".join([i_ans[0] + " " + i_ans[1] for i_ans in words_list])
open('analysis.txt', 'w').write(string_answer)

