"""
Given an integer array nums sorted in non-decreasing order, 

return an array of the squares of each number sorted in non-decreasing order.
"""

def sorted_squares(nums):
    result = [0] * len(nums) # create a list of zeroes initilized to the size of nums
    write = len(nums) - 1 # third pointer to add values into the list
    left = 0
    right = len(nums) -1
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square >= right_square:
            result[write] = left_square
            left += 1
            write -= 1
        else:
            result[write] = right_square
            right -= 1
            write -= 1

    return result


# Test cases
print(sorted_squares([-4, -1, 0, 3, 10]))
# Expected: [0, 1, 9, 16, 100]

print(sorted_squares([-7, -3, 2, 3, 11]))
# Expected: [4, 9, 9, 49, 121]

print(sorted_squares([-5, -3, -2, -1]))
# Expected: [1, 4, 9, 25]

print(sorted_squares([1, 2, 3, 4]))
# Expected: [1, 4, 9, 16]

print(sorted_squares([0]))
# Expected: [0]