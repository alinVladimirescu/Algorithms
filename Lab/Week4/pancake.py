def flip(arr, k):
    new_arr = arr[:k + 1]
    new_arr = new_arr[::-1]
    new_arr.extend(arr[k+1:])
    return new_arr
def find_max_unsorted(arr, end):
    max_idx = 0
    for i in range(1, end + 1):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def pancake_sort(arr):
    for end in range(len(arr) - 1, 0, -1):
        max_idx = find_max_unsorted(arr, end)
        if max_idx == end:
            continue
        if max_idx != 0:
            arr = flip(arr, max_idx)

        arr = flip(arr, end)
    return arr
        
