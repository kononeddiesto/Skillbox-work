def QHofstadter(n: list):
    if len(n) == 2 and n[0] == 1 and n[1] == 1:
        Q = n
        for i in range(2, 20):
            Q.append(Q[i - Q[i - 1]] + Q[i - Q[i - 2]])
            yield Q
    else:
        return


for index in QHofstadter([1, 1]):
    print(index)
