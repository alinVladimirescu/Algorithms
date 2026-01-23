input = [1, 2, 3, 4]


def binary_search_max(l, r):
    while l <= r:
        mid = (l + r) // 2
        if mid == 0 or mid == len(input) - 1:
            return input[mid]
        if input[mid] >= input[mid + 1] and input[mid] >= input[mid - 1]:
            return input[mid]
        elif input[mid] < input[mid + 1]:
            l = mid + 1
        else:
            r = mid - 1
def binary_search(arr, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            print("Found")
            return
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
maxi = binary_search_max(0, len(input) - 1)
index_maxi = input.index(maxi)
reg_half = input[:index_maxi]
second_half = input[index_maxi:]
reversed_half = second_half[::-1]
target = 2
binary_search(reg_half,0, len(reg_half) - 1, target)
binary_search(reversed_half,0, len(reversed_half) - 1, target)
    