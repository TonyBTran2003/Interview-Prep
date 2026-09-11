"""
You are given an unsorted list of integers days, where each integer represents a day on which a user was active.

Return the length of the longest sequence of consecutive days.

The numbers do not need to appear next to each other in the original list.
"""

def longest_activity_streak(days):
    day_set = set(days) # lookups take o(1)
    longest = 0 # this variable will hold the longest sequence
    for day in day_set:
        if day -1 not in day_set: #if the previous day not in set then it is the start of a sequence
            current_day = day # variable to keep track of current day so we dont edit the other loop
            current_length = 1 # keep track of length
            while current_day + 1 in day_set: # check if the next day is in the set
                current_day += 1 # if yes adjust current day and length
                current_length += 1

            longest = max(longest, current_length) # keep track of longest

    return longest #return longest




print(longest_activity_streak([100, 4, 200, 1, 3, 2]))
# Expected: 4

print(longest_activity_streak([9, 1, 4, 7, 3, 2, 6, 5]))
# Expected: 7

print(longest_activity_streak([5, 5, 6, 7]))
# Expected: 3

print(longest_activity_streak([]))
# Expected: 0