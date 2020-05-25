def solution(N):
    """ This function first creats the interger to 
    binary representation and then calculates number 
    of binary gaps in the binary representation of N"""
    binary_rep = []
    one_index = []
    binary_gap = []
    while N >= 1:
        remainder = N % 2
        N = round(N / 2)
        binary_rep.append(remainder)
    binary_rep.reverse()
    print(binary_rep)
    one_index = [i for i, e in enumerate(binary_rep, 1) if e == 1]
    if len(one_index) == 1:
        return 'No Binary gaps'
    binary_gap = max([j-i for i, j in zip(one_index[:-1], one_index[1:])])
    binary_gap = binary_gap - 1

    return binary_gap

binary_gap = solution(15)
