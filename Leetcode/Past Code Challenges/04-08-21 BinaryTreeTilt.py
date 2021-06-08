# Leetcode #563 - Binary Tree Tilt

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node val={self.val}, left={self.left}, right={self.right}"


def sumOfTree(node):
    if not node:
        return 0
    value = node.val
    return value + sumOfTree(node.left) + sumOfTree(node.right)


def findTilt(root: TreeNode) -> int:

    if not root:
        return 0

    nodeTilt = abs(sumOfTree(root.left) - sumOfTree(root.right))
    return nodeTilt + findTilt(root.left) + findTilt(root.right)


node2 = TreeNode(10)
node3 = TreeNode(20)
node1 = TreeNode(30, node2, node3)

print(sumOfTree(node1))

# TreeNode{val: 21, left: TreeNode{val: 7, left: TreeNode{val: 1, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}, right: TreeNode{val: 1, left: None, right: None}}, right: TreeNode{val: 14, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}}}
