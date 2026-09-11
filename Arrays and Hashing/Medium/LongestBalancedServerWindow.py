"""
Problem: Longest Balanced Server Window

A monitoring system records server results as:

1 = successful request
0 = failed request

You are given an array requests.

Return the length of the longest contiguous section that contains the same number of successful and failed requests.
"""

def longest_balanced_window(requests):
    balance = 0
    longest = 0
    first_seen = {0: -1}

    for index, request in enumerate(requests):
        if request == 0:
            balance -= 1
        else:
            balance += 1

        if balance in first_seen:
            current_length = index - first_seen[balance]
            longest = max(longest, current_length)
        else:
            first_seen[balance] = index

    return longest
                
            

print(longest_balanced_window([1, 0]))
# Expected: 2

print(longest_balanced_window([1, 1, 0, 1, 0, 0]))
# Expected: 6

print(longest_balanced_window([1, 1, 1, 0, 0]))
# Expected: 4

print(longest_balanced_window([1, 1, 1]))
# Expected: 0

print(longest_balanced_window([]))
# Expected: 0