"""
A company records purchases as a list of customer IDs:

transactions = [4, 2, 7, 4, 8, 2]

You are given an integer k.

A transaction is considered suspicious if the same customer ID appears twice within k positions of each other.

Return True if there is at least one suspicious pair. Otherwise, return False.

"""

def suspicious_transactions(transactions, k):
    seen = {}
    for index, action in enumerate(transactions):
        if action in seen:
            if index - seen[action] <= k:
                return True
        seen[action] = index

    return False



print(suspicious_transactions([4, 2, 7, 4, 8], 3))
# Expected: True

print(suspicious_transactions([1, 2, 3, 1], 2))
# Expected: False

print(suspicious_transactions([5, 5], 1))
# Expected: True

print(suspicious_transactions([1, 2, 3, 4, 1], 3))
# Expected: False