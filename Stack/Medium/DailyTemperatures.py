"""
Given a list temperatures, return a list answer where:

answer[i] = number of days you have to wait
            until a warmer temperature

If there is no warmer future day, use 0.
"""

def daily_temperatures(temperatures):
    # Your code here
    pass


# Test cases
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# Expected: [1, 1, 4, 2, 1, 1, 0, 0]

print(daily_temperatures([30, 40, 50, 60]))
# Expected: [1, 1, 1, 0]

print(daily_temperatures([30, 60, 90]))
# Expected: [1, 1, 0]

print(daily_temperatures([90, 80, 70, 60]))
# Expected: [0, 0, 0, 0]

print(daily_temperatures([70]))
# Expected: [0]

print(daily_temperatures([70, 70, 71]))
# Expected: [2, 1, 0]