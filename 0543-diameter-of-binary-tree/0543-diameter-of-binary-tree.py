# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(node):
            if node is None:
                return 0
            node.val = 1 + max(maxDepth(node.right), maxDepth(node.left))
            return node.val
        maxDepth(root)
        
        def diameter(node):
            if node is None:
                return 0
            cur = 0
            if node.left: cur += node.left.val
            if node.right: cur += node.right.val
            return max(diameter(node.left), diameter(node.right), cur)
        
        return diameter(root)