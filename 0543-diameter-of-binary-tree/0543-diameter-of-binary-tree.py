# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def maxDepth(node):
            if node is None:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))
        
        maxCur = 0
        if root.left: maxCur += maxDepth(root.left)
        if root.right: maxCur += maxDepth(root.right)
        
        return max(maxCur, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))