# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Height of left and right subtrees should not be > 1
        
        def maxDepth(node):
            if node is None: return 0
            node.val = 1 + max(maxDepth(node.left), maxDepth(node.right))
            return node.val
        
        if root is None:
            return True
        
        cur = abs(maxDepth(root.left) - maxDepth(root.right)) < 2
        return cur and self.isBalanced(root.right) and self.isBalanced(root.left)
            