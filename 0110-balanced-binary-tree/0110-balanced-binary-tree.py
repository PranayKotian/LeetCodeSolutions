# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #determine balance while calculating maxdepth
        self.balanced = True
        def maxDepth(node):
            if node is None: return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            if abs(left-right) >= 2:
                self.balanced = False
            return 1 + max(left,right)
        maxDepth(root)
        
        return self.balanced