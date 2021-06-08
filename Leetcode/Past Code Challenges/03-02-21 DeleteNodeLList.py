class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.

    Delete a given node, delete this node without having access to head of the list.
    """
    
    node.val = node.next.val
    node.next = node.next.next