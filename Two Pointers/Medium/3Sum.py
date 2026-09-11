"""
Given an integer array nums, return all unique triplets:

[nums[i], nums[j], nums[k]]

such that:

nums[i] + nums[j] + nums[k] == 0

The solution must not contain duplicate triplets.
"""

def three_sum(nums):
    result = []

    nums.sort()
    index = 0
    left = 1
    right = len(nums) - 1
    for index, num in enumerate(nums):
        if index > 0 and nums[index] == nums[index - 1]: #checks to see if the last number was the same as current if yes, then skip
            continue
        left = index + 1
        right = len(nums) - 1
        while left < right:
            if num + nums[left] + nums[right] == 0: #if == 0 then append to list and then move on
                result.append([num, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif num + nums[left] + nums[right] > 0: # if more than 0 only move the right pointer
                right -= 1

            else:
                left += 1 # if less than 0 only move the left
    
    return result


# Test cases
print(three_sum([-1, 0, 1, 2, -1, -4]))
# Expected: [[-1, -1, 2], [-1, 0, 1]]
# Order may vary

print(three_sum([0, 1, 1]))
# Expected: []

print(three_sum([0, 0, 0]))
# Expected: [[0, 0, 0]]

print(three_sum([-2, 0, 1, 1, 2]))
# Expected: [[-2, 0, 2], [-2, 1, 1]]

print(three_sum([]))
# Expected: []