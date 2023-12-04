#https://leetcode.com/problems/balanced-binary-tree/
#Title: 110. Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #EFFICIENT SOLUTION - merges isBalanced check into depth function
        def depth(root):
            if root is None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            if left == -1 or right == -1 or abs(left-right) >= 2:
                return -1
            return max(left, right) + 1
        
        return depth(root) != -1
    
        '''
        #MY SOLUTION
        def depth(root):
            if root is None:
                return 0
            return max(depth(root.left), depth(root.right)) + 1
        
        if root is None:
            return True
        return abs(depth(root.left)- depth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        '''