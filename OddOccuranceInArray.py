def solution(A):
    result = 0
    for number in A:
        result ^= number
    return result

arr_ = [9,3,9,3,9,7,9]
solution(arr_)