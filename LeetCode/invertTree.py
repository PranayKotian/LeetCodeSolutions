#https://leetcode.com/problems/invert-binary-tree/
#Title: 226. Invert Binary Tree
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        '''
        PSEUDOCODE
        copy left node
        left node now right node
        copy backup of left node into right node
        go down recursively
        '''
        
        if not root:
            return root
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
            
        return root