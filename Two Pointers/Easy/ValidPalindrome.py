"""
Given a string s, return True if it is a palindrome, or False otherwise.

A palindrome reads the same forward and backward.

For this problem, ignore:

spaces
punctuation
capitalization
"""

def is_palindrome(s):
    left = 0
    right = len(s) -1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
                    right -= 1

        if s[left].lower() != s[right].lower():
              return False

        else:
              left += 1
              right -= 1

    return True

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))
# Expected: True

print(is_palindrome("race a car"))
# Expected: False

print(is_palindrome(" "))
# Expected: True

print(is_palindrome("Madam"))
# Expected: True

print(is_palindrome("0P"))
# Expected: False