"""
You are given an integer array height of length n.

Each value represents the height of a vertical line.

You want to choose two lines that, together with the x-axis, form a container that holds the most water.

Return the maximum amount of water.

"""

def max_area(height):
    largest = 0 # store the largets area
    left = 0
    right = len(height) - 1
    while left < right:
        cur_result = min(height[left], height[right]) * (right - left)
        largest = max(largest, cur_result)

        if height[right] > height[left]: # if the right is currently larger than left move the left pointer to potentially find a larger left
            left += 1
        else:
            right -= 1 # same logic as above

    return largest



# Test cases
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# Expected: 49

print(max_area([1, 1]))
# Expected: 1

print(max_area([4, 3, 2, 1, 4]))
# Expected: 16

print(max_area([1, 2, 1]))
# Expected: 2

print(max_area([2, 3, 4, 5, 18, 17, 6]))
# Expected: 17