# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        #Recursive Solution
        #Time: O(n) Space: O(n)
        
        if root.left is None and root.right is None:
            return True if root.val == 1 else False
        else:
            if root.val == 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            else: #root.val == 3
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)