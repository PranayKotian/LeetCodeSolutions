# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        #Solution 2: Recursive Solution w/ Helper Function
        #Time: O(n) Space: O(n) or O(logn) if balanced tree
        
        if root is None:
            return False
        
        def dfs(node, cur):
            if node == None:
                return False
            cur += node.val
            if node.left is None and node.right is None:
                return cur == targetSum
            return dfs(node.left, cur) or dfs(node.right, cur)
        
        return dfs(root, 0)
        
        """
        #Solution 1: Recursive Solution
        #Time: O(n) Space: O(n) or O(logn) if balanced tree
        
        #Base Cases
        if root == None:
            return False
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        
        #Recursive Case
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        """