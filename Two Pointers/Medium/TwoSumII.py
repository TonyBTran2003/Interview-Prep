"""
You are given a 1-indexed sorted array numbers and an integer target.

Find two numbers such that they add up to target.

Return their 1-based indices:

[index1, index2]

You may assume:

exactly one solution exists
you cannot use the same element twice

""" 

def two_sum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        elif numbers[l] + numbers[r] > target:
            r -= 1

        else:
            l+= 1
        


# Test cases
print(two_sum([2, 7, 11, 15], 9))
# Expected: [1, 2]

print(two_sum([2, 3, 4], 6))
# Expected: [1, 3]

print(two_sum([-1, 0], -1))
# Expected: [1, 2]

print(two_sum([1, 2, 3, 4, 6], 6))
# Expected: [2, 4]

print(two_sum([-5, -2, 0, 3, 8], 6))
# Expected: [2, 5]