#https://leetcode.com/problems/subtree-of-another-tree/
#Title: 572. Subtree of Another Tree
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
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
        
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        elif not q or not p:
            return False
        
        if (p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else: #p.val != q.val
            return False