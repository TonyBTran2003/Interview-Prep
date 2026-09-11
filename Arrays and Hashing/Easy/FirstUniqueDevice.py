"""
You are given a list of strings devices, where each string is a device ID.

Return the index of the first device ID that appears exactly once in the list.

If every device ID appears more than once, return -1.

"""


def first_unique_device(devices):
    count_dev = {}

    for device in devices:
        count_dev[device] = count_dev.get(device, 0) + 1

    for index, item in enumerate(devices):
        if count_dev[item] == 1:
            return index

    return -1


print(first_unique_device(["A1", "B2", "A1", "C3", "B2"]))
# Expected: 3

print(first_unique_device(["X", "Y", "X", "Y"]))
# Expected: -1

print(first_unique_device(["Z"]))
# Expected: 0

print(first_unique_device(["A", "B", "C", "A", "B"]))
# Expected: 2