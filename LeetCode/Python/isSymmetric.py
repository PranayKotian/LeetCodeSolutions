#https://leetcode.com/problems/symmetric-tree/
#Title: 101. Symmetric Tree
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(level):
            if level == [] or all(v is None for v in level):
                return True
            
            templevel = []
            nextlevel = []
            
            for node in level:
                if node:
                    templevel.append(node.val)
                    nextlevel.append(node.left)
                    nextlevel.append(node.right)
                else:
                    templevel.append("Null")
            return (templevel == templevel[::-1]) and bfs(nextlevel)
            
            
        return bfs([root])