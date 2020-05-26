def cyclic(arr, k):
    if k == len(arr):
        return arr
    new_i_index = 0
    new_arr = []
    for i, value in enumerate(arr):
        new_i_index = (i+k) % len(arr)
        new_arr.insert(new_i_index, value)

    return new_arr

a = [7,2,3,8,5]
arr = cyclic(a, 2)