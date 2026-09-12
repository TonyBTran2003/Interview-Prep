"""
Remove Nth Node From End of List

You are given the head of a singly linked list and an integer n.

Remove the nth node from the end of the list and return the head.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    for _ in range(n+1): # +1 because we have a dummy/empty node before numbers
        if fast is None:
            break
        fast = fast.next
    

    while fast: #when fast reaches the end of the list 
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next #replace next value(delete value) with the next next value

    return dummy.next

    

def build_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# Test 1
head = build_list([1, 2, 3, 4, 5])
head = remove_nth_from_end(head, 2)
print(print_list(head))
# Expected: [1, 2, 3, 5]


# Test 2
head = build_list([1])
head = remove_nth_from_end(head, 1)
print(print_list(head))
# Expected: []


# Test 3
head = build_list([1, 2])
head = remove_nth_from_end(head, 1)
print(print_list(head))
# Expected: [1]


# Test 4
head = build_list([1, 2])
head = remove_nth_from_end(head, 2)
print(print_list(head))
# Expected: [2]