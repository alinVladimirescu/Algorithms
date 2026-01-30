def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr
def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quick_sort(arr, l = 0, h = None):
    if h is None:
        h = len(arr) - 1
    if l < h:
        pivot_i = partition(arr, l, h)
        quick_sort(arr, l, pivot_i - 1)
        quick_sort(arr, pivot_i + 1, h)

def quick_sort_stack(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        l, h = stack.pop()
        if l < h:
            pivot_i = partition(arr, l, h)
            if pivot_i < h:
                stack.append((pivot_i + 1, h))
            else:
                stack.append((l, pivot_i - 1))
        
        
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
sorted_arr = [8,2,4,7,1,3,9,6,5]
quick_sort(sorted_arr)
print(sorted_arr)