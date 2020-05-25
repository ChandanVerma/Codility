### Correctness 80%
def solution(N):
    """ This function first creats the interger to 
    binary representation and then calculates number 
    of binary gaps in the binary representation of N"""
    current_gap = 0
    max_gap = 0
    while (N > 0 and N%2 ==0):
        N //= 2

    while N > 0:
        remainder = N%2
        if remainder == 0:
            current_gap += 1
        elif remainder == 1:
            max_gap = max(current_gap, max_gap)
            current_gap = 0
        
        N //= 2

    return binary_gap
