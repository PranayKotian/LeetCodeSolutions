#https://leetcode.com/problems/maximum-depth-of-binary-tree/
#Title: 104. Maximum Depth of Binary Tree
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
    def maxDepth(self, root: TreeNode) -> int:
        
        #recursive solution
        if not root:
            return 0
        if (root.left == None and root.right == None):
            return 1
        elif (root.left == None):
            return self.maxDepth(root.right) + 1
        elif (root.right == None):
            return self.maxDepth(root.left) + 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        
        