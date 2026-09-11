"""
Two engineering teams maintain sorted lists of software build numbers.

You are given two sorted integer arrays:

team_a
team_b

Return a list containing the build numbers that appear in both arrays.

Each build number should appear only once in the result, even if it appears multiple times in the inputs.
"""


def common_builds(team_a, team_b):
    result = []
    team_a_pointer = 0
    team_b_pointer = 0
    while team_a_pointer < len(team_a) and team_b_pointer < len(team_b):
        if team_a[team_a_pointer] == team_b[team_b_pointer]:
            if not result or result[-1] != team_a[team_a_pointer]:
                result.append(team_a[team_a_pointer])

            team_a_pointer += 1
            team_b_pointer += 1

        elif team_a[team_a_pointer] > team_b[team_b_pointer]:
            team_b_pointer += 1
        elif team_a[team_a_pointer] < team_b[team_b_pointer]:
            team_a_pointer += 1
                    
        
    return result
print(common_builds(
    [1, 2, 4, 6, 8],
    [2, 3, 4, 7, 8]
))
# Expected: [2, 4, 8]


print(common_builds(
    [1, 1, 2, 3, 5],
    [1, 1, 3, 4, 5]
))
# Expected: [1, 3, 5]


print(common_builds(
    [1, 2, 3],
    [4, 5, 6]
))
# Expected: []