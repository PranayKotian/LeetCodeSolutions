# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        #Solution 1: Recursive Solution
        #Time: O(n) Space: O(1)
        
        #Base Cases
        if root == None:
            return False
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        
        #Recursive Case
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)