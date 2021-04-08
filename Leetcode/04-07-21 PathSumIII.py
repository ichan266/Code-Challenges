# LeetCode #437
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def count_paths(self, root, sum):
        """ Taken in a node (root) and an integer (sum), return total # of paths summing up to sum starting with root. """
        
        if root == None:
            return 0
        
        path_count = 0
        
        sum -= root.val
        if sum == 0:
            path_count += 1
            
        path_count += self.count_paths(root.left, sum) # we want to use this "new" sum so it won't subtract from 8 all the time
        path_count += self.count_paths(root.right, sum)
        
        return path_count
    
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        if root == None:
            return 0
        
        path_count = self.count_paths(root, sum)
        path_count += self.pathSum(root.left, sum)
        path_count += self.pathSum(root.right, sum)
        
        return path_count

instance = Solution()
print(instance.pathSum(None, 0))