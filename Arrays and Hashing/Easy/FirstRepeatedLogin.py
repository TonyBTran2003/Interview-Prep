"""
You are given an array of strings logins, where each string represents a username logging into a system.

Return the index of the first login that belongs to a user who has already logged in before.

If no username appears more than once, return -1.
"""

def first_repeated_login(logins):
    seenNames = set()
    for index, name in enumerate(logins):
        if name in seenNames:
            return index
        seenNames.add(name)
    return -1
        



# Test cases
print(first_repeated_login(["alice", "bob", "charlie", "bob", "david"]))
# Expected: 3

print(first_repeated_login(["sam", "jordan", "alex"]))
# Expected: -1

print(first_repeated_login(["amy", "amy", "bob", "bob"]))
# Expected: 1

print(first_repeated_login(["a", "b", "c", "a", "b"]))
# Expected: 3