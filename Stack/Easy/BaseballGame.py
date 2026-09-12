"""
You are keeping score for a baseball game with unusual rules.

You are given a list of strings operations, where each string is one of:

an integer x → record a new score of x
"+" → record a new score equal to the sum of the previous two scores
"D" → record a new score equal to double the previous score
"C" → remove the previous score

Return the total sum of all scores after performing every operation.
"""

def cal_points(operations):
    stack = []
    total = 0
    for operation in operations:
        if operation == 'C':
            stack.pop()
        elif operation == 'D':
            stack.append(2 * stack[-1])
        elif operation == '+':
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(operation))

    return sum(stack)


# Test cases
print(cal_points(["5", "2", "C", "D", "+"]))
# Expected: 30

print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))
# Expected: 27

print(cal_points(["1", "C"]))
# Expected: 0

print(cal_points(["10", "20", "+", "D"]))
# Expected: 120