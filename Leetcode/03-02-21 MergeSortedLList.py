# Leetcode #21
# Easy
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):

    head = ListNode()
    walk = head  # Head starts at 0 when we instantiate a new ListNode Class by default

    while l1 and l2:
        if l1.val <= l2.val:
            walk.next = l1
            walk = walk.next
            l1 = l1.next
        elif l1.val > l2.val:
            walk.next = l2
            walk = walk.next
            l2 = l2.next

    if l1:
        walk.next = l1

    if l2:
        walk.next = l2

    return head.next


def mergeTwoLists1(l1, l2):

    if not l1 and not l2:
        return
    elif not l1 and l2:
        return l2
    elif not l2 and l1:
        return l1

    if l1.val <= l2.val:
        combineHead = l1
    elif l2.val < l1.val:
        combineHead = l2

    head_1, tail_1 = l1, l1.next
    head_2, tail_2 = l2, l2.next

    while head_1 and head_2:
        if head_1.val <= head_2.val:
            head_1.next = head_2
            head_1 = tail_1
            if tail_1 is not None:
                tail_1 = tail_1.next
        elif head_1.val > head_2.val:
            head_2.next = head_1
            head_2 = tail_2
            if tail_2 is not None:
                tail_2 = tail_2.next

    print(f"head_1={head_1}")
    print(f"head_2={head_2}")

    if head_1 or (not head_1 and not head_2):
        head_2 = head_1
    elif head_2:
        head_1 = head_2

    return combineHead
