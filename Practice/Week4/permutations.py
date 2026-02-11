arr1 = [1,2,3]
arr2 = [3,2,1]
def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    sorted_right = merge(right)
    sorted_left = merge(left)
    return merge_sorted(sorted_left, sorted_right)

def merge_sorted(arr1, arr2):
    sorted_arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    sorted_arr.extend(arr1[i:])
    sorted_arr.extend(arr2[j:])
    return sorted_arr

def check_permutations(arr1, arr2):
    return merge(arr1) == merge(arr2)

print(check_permutations(arr1, arr2))