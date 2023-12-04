#https://leetcode.com/problems/binary-tree-tilt/
#Title: 563. Binary Tree Tilt
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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def tilt(node):
            if node is None:
                return
            
            node.val = abs(sumtree(node.left) - sumtree(node.right))
            tilt(node.left)
            tilt(node.right)
        
        def sumtree(node):
            if node is None:
                return 0
            return node.val + sumtree(node.left) + sumtree(node.right)
        
        tilt(root)
        return sumtree(root)