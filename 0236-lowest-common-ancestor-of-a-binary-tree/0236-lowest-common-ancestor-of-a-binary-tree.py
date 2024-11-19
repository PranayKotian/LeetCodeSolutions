# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #Recursive Solution
        #Time: O(n) Space: O(h)
        
        if root is None:
            return None
        if root == p or root == q:
            return root
        
        p1 = self.lowestCommonAncestor(root.left, p, q)
        p2 = self.lowestCommonAncestor(root.right, p, q)
        
        if p1 is None and p2 is None:
            return None
        if p1 and p2:
            return root
        if p1: return p1
        if p2: return p2