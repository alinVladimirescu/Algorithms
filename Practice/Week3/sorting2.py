def bubble_sort(arr):
    sorted = 0
    while not sorted:
        sorted = 1
        for i in range(len(arr) - 1):
            if(arr[i] > arr[i + 1]):
                sorted = 0
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def bucket_sort(arr):
    buckets = [[] for _ in range(10)]
    for i, num in enumerate(arr): 
        buckets[int(10 * arr[i])].append(num)
    for bucket in buckets:
        bubble_sort(bucket)
        index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

    return arr

print(bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]))