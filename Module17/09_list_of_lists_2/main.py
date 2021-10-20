nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [elem for one_list in nice_list for two_list in one_list for elem in two_list]

print(new_list)
