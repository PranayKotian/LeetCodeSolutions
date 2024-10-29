# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        #Iterative Solution - DFS
        #Time: O(n) Space: O(n)
        
        stack = [[root, targetSum]]
        while stack:
            node,tar = stack.pop()
            if node is None:
                continue
            if node.left is None and node.right is None and node.val == tar:
                return True
            stack.append([node.left, tar-node.val])
            stack.append([node.right, tar-node.val])
        return False
        
        """
        #Recursive Solution
        #Time: O(n) Space: O(h) 
        
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        """