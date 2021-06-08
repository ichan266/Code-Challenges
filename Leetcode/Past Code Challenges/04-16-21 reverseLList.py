# Leetcode #206
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
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

class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        
        new_head = None
        
        while head:
            temp = head
            head = head.next
            temp.next = new_head
            new_head = temp
            
        return new_head           