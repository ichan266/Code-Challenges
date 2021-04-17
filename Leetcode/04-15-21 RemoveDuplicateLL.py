# Leetcode #83
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        current = head
        
        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
                
        return head

instance = Solution()

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        curr = head
        
        if curr == None or curr.next == None:
            return curr
        
        while curr!= None and curr.next!= None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
