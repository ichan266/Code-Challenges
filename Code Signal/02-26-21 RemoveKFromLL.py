class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} -> {self.next}"


def removeKFromList(l, k):

    # This handle cases with k being at the front of the linked list. It sets
    # the head to whenever it found
    while l != None and l.value == k:
        l = l.next
            
    if l == None:
        return l
    
    front = l
    tail = l.next

    while tail != None:
        if tail.value != k:
            front.next = tail
            front = tail
        tail = tail.next
        if tail == None:
            front.next =  tail
            
    return l  
    

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
print(removeKFromList(head, 2))
