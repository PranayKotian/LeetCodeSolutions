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
        
        def invert(node):
            if node is None:
                return

            temp = node.left
            node.left = node.right
            node.right = temp

            invert(node.left)
            invert(node.right)
        
        invert(root)
        
        return root

        '''
        #OLD SOLUTION
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
        '''