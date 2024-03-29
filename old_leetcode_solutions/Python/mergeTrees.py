#https://leetcode.com/problems/merge-two-binary-trees/
#Title: 617. Merge Two Binary Trees
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
            
            if root1 is None and root2 is None:
                return None
            elif root1 is None:
                return root2
            elif root2 is None:
                return root1
            
            node = TreeNode()
            node.val = root1.val + root2.val
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node