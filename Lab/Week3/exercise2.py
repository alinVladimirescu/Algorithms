# Exercise 2 – Separate positive and negative numbers
# Given a list of both positive and negative numbers in random order, design and implement an efficient algorithm to rearrange the array elements so that positive and negative numbers are placed alternatively, starting from a positive number, and so that positives are sorted and negatives are sorted. If there are more negative or positive numbers, they should be placed at the end of the rearranged list (for this latter part, the order in which numbers appear is not important). 

# Example:
# Given [-8, 1, 2, -4, 6, 12, 5, -10, 16, 7, 11], the algorithm should output: 
# [1, -4, 6, -8, 12, -10, 5, 2, 16, 7, 11]
nums = [-8, 1, 2, -4, 6, 12, 5, -10, 16, 7, 11]
def arrange_numbers(nums):
    pos_nums = []
    neg_nums = []
    for n in nums:
        if n > 0:
            pos_nums.append(n)
        else:
            neg_nums.append(n)
    pos_nums.sort()
    neg_nums.sort(reverse = True)
    i = j = 0
    counter = 0
    res = []
    while i < len(pos_nums) and j < len(neg_nums):
        if counter % 2 == 1:
           res.append(neg_nums[j])
           j += 1
        else:
            res.append(pos_nums[i])
            i += 1
        counter += 1
    
    while i < len(pos_nums):
        res.append(pos_nums[i])
        i += 1
    while j < len(neg_nums):
        res.append(neg_nums[j])
        j += 1
    return res

print(arrange_numbers(nums))