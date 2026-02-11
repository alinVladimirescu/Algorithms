def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) //2
    right = arr[mid:]
    left = arr[:mid]
    sorted_left = merge(left)
    sorted_right = merge(right)
    return merge_sort(sorted_left, sorted_right)
def merge_sort(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
def process_times(times):
    interval = []
    for start, end in times:
        interval.append(end - start + 1)
    interval = merge(interval)
    return interval[0], interval[len(interval) - 1]
times = [(1, 10), (2, 10), (1,2)]
print(process_times(times))