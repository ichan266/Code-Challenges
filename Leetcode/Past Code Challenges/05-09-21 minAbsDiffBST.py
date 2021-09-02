# Leetcode # 530
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

def getMinimumDifference(root):
    prev, minDiff = None, None

    def visit(root):
        nonlocal prev
        nonlocal minDiff
        if root.left:
            visit(root.left)
        if prev != None:
            if minDiff != None:
                minDiff = min(minDiff, root.val-prev)
            else:
                minDiff = root.val - prev
        prev = root.val
        if root.right:
            visit(root.right)

    visit(root)

    return minDiff

# % Pair programming with Ben. Took about 2 hours together to work through this problem
