# Leetcode #206
# Easy
# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# * This one just put all the nodes in a list, then change the pointer the other direction in order to reverse the linked list
def reverseList1(head):

    if not head or not head.next:
        return head

    current = head
    llist = []

    while current:
        llist.append(current)
        current = current.next

    for index in range(len(llist)-1, 0, -1):
        llist[index].next = llist[index-1]

    head = llist[-1]
    llist[0].next = None

    return head

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# * This is the most classic one. It is a bit of mental exercise.
# * Bottom line: make sure to assign variables pointing to the right nodes, followed by changing the pointers (i.e. `.next`), then reassign the variables to the right nodes for the next loop.


def reverseList2(head):

    new_head = None

    while head:
        walk = head.next
        head.next = new_head
        new_head = head
        head = walk

    return new_head

# @ We first start with assigning new_head to None so the very first iteration of the while loop will have head points to None
# @ Enter while loop if head is not None:
# @  1. Assign walk to the next node after head
# @  2. Now with two variables of head pointing to the current node and walk pointing to the node after head, we can change the head.next pointer:
# @      We want head.next point to new_node (which is None now)
# @  3. Once head.next next is all set, we start to reassign the variables of new_head and head:
# @      a. Make new_head equals to head (so now it is no longer None)
# @      b. Make head equals to walk
# @ Steps are repeat until the head == None
# % Please note new_head works by reassigning head to new_head. If we are at the end of the list, when head moves to walk, it will become None, it will then exit the while loop

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


def reverseListRecur(head):
    if not head or head.next:
        return head

    new_head = reverseListRecur(head.next)
    head.next.next = head
    head = None

    return new_head
