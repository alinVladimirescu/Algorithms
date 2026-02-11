def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    right = arr[mid:]
    left = arr[:mid]
    sorted_right = merge(right)
    sorted_left = merge(left)
    return merge_sort(sorted_right, sorted_left)
def merge_sort(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if ord(left[i]) < ord(right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def compare_strings(string1, string2, string3):
    string1 = merge(list(string1))
    string1 = "".join(string1)
    string2 = merge(list(string2))
    string2 = "".join(string2)
    string3 = merge(list(string3))
    string3 = "".join(string3)
    min_len = min(len(string1), len(string2), len(string3))
    min_string = ""
    if len(string1) == min_len:
        min_string = string1
    elif len(string2) == min_len:
        min_string = string2
    else:
        min_string = string3
    res = [c for c in min_string if c in string1 and c in string2 and c in string3]
    res = "".join(res)
    return res

print(compare_strings("abbcd", "cda", "accccccccdcc"))
