"""
Given a string s containing only these characters:

( ) { } [ ]

return True if the string is valid.

A string is valid if:

every opening bracket has the correct closing bracket
brackets close in the correct order
"""

def is_valid(s):
    pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    stack = []
    for char in s:
        if char in pairs:
            if len(stack) == 0:
                return False

            cur = stack.pop()

            if pairs[char] != cur:
                return False

        else:
            stack.append(char)
            
    return not stack


# Test cases
print(is_valid("()"))
# Expected: True

print(is_valid("()[]{}"))
# Expected: True

print(is_valid("(]"))
# Expected: False

print(is_valid("([)]"))
# Expected: False

print(is_valid("{[]}"))
# Expected: True

print(is_valid("]"))
# Expected: False