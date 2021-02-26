class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"


def middleNode(head):

    listNode = []

    walk = head

    while walk != None:
        listNode.append(walk)
        walk = walk.next

    mid = len(listNode)//2

    return listNode[mid]
    

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
print(middleNode(head))
