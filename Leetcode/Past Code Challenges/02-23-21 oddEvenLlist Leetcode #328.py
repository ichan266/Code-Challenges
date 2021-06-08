# LeetCode #328

# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the value
# in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity
# and O(nodes) time complexity.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


def oddEvenList(head: ListNode):

    if head == None or head.next == None or head.next.next == None:
        return head

    connection = head.next

    oddHead = head
    evenHead = head.next
    tail = head.next.next

    while True:
        oddHead.next = evenHead.next
        evenHead.next = tail.next
        oddHead = oddHead.next
        evenHead = evenHead.next
        if evenHead == None or evenHead.next == None:
            break
        tail = evenHead.next

    oddHead.next = connection

    return head


a1 = ListNode(2)
b2 = ListNode(1)
c3 = ListNode(3)
d4 = ListNode(5)
e5 = ListNode(6)
f6 = ListNode(4)
g7 = ListNode(7)
h8 = ListNode(0)

head = a1
a1.next, b2.next, c3.next = b2, c3, d4
d4.next, e5.next, f6.next = e5, f6, g7
g7.next = h8
print(oddEvenList(head))
