import random
import time

arr = [1,2,3,4,5]
target = 1
ranges = [1000, 2000, 4000, 8000, 16000]

def linear_search(arr, target):
    iterations = 0
    for num in arr:
        if num == target:
            return True, iterations
        iterations += 1
    return False, iterations
    


def binary_search(arr, target):
    iterations = 0
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return True, iterations
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        iterations += 1
    return False

def trinary_search(arr, target):
    iterations = 0
    l, m, r = 0, len(arr) // 2, len(arr) - 1
    while l <= m <= r:
        one_third, two_third = (l + m) // 2, (r + m) // 2
        if arr[one_third] == target or arr[two_third] == target:
            return True, iterations
        if target < arr[one_third]:
            r = one_third - 1
            m = (l + r) // 2
        elif target < arr[two_third]:
            r = two_third - 1
            l = one_third + 1
            m = (l + r) // 2
        else:
            l = two_third + 1
            m = (l + r) // 2
        iterations += 1
    return False

def generate_test_arr(ranges):
    index = random.randrange(1, 5)
    return sorted([random.randrange(ranges[index - 1], ranges[index]) for _ in range(10000)])

def generate_random_target(arr):
    return random.choice(arr)


def test_search(arr):
    arr = generate_test_arr(ranges)
    target = generate_random_target(arr)
    start = time.time()
    _, iterations = linear_search(arr, target)
    print(f"linear_search took: {time.time() - start}")
    print(f"number of iterations = {iterations}")
    start = time.time()
    _, iterations = binary_search(arr, target)
    print(f"binary search took: {time.time() - start}")
    print(f"number of iterations: {iterations}")
    start = time.time()
    _, iterations = trinary_search(arr, target)
    print(f"trinary search took: { time.time() - start}")
    print(f"number of iterations: {iterations}")

test_search([])


