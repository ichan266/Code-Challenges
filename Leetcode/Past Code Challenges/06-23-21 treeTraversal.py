# Leetcode 94, 144, 145
# PreOrder #144: https://leetcode.com/problems/binary-tree-preorder-traversal/
# InOrder #94: https://leetcode.com/problems/binary-tree-inorder-traversal/
# PostOrder #145: https://leetcode.com/problems/binary-tree-postorder-traversal/

# Return a list of nodes' values in pre-order, in-order, and post-order in a binary tree


def preorderTraversal(root):

    if not root:
        return []

    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)


def inorderTraversal(root):

    if not root:
        return []

    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


def postorderTraversal(root):

    if not root:
        return []

    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]
