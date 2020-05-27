def solution(A):
    left_arr = []
    right_arr = []
    min_abs_diff = 0
    abs_diff = 0
    for i, value in enumerate(A, 1):
        if i == 1:
            left_arr = [A[0]]
            right_arr = A[1:]
            abs_diff = abs(sum(left_arr) - sum(right_arr))
            min_abs_diff = abs_diff
        else:
            left_arr = A[:i]
            right_arr = A[i:]
            abs_diff = abs(sum(left_arr) - sum(right_arr))
            min_abs_diff = min(abs_diff, min_abs_diff)

    return min_abs_diff

a = [3,1,2,4,3]
min_ = solution(a)