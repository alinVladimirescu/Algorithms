def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    right_arr = arr[mid:]
    left_arr = arr[:mid]

    sorted_left = mergeSort(left_arr)
    sorted_right = mergeSort(right_arr)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(mergeSort([1, 2, 3, 4, 7, 10, 5]))
