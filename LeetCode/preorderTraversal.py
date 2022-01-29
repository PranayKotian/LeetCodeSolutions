#https://leetcode.com/problems/binary-tree-preorder-traversal/
#Title: 144. Binary Tree Preorder Traversal
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #ITERATIVE SOLUTION
        if root is None:
            return [] 
        
        stack = [root]
        res = []
        
        while stack != []:
            root = stack.pop()
            res.append(root.val)
            if (root.right is not None):
                stack.append(root.right)
            if (root.left is not None):
                stack.append(root.left)
        
        return res
        
        '''
        #RECURSIVE SOLUTION
        if root is None:
            return []
        return ([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))
        '''
        '''