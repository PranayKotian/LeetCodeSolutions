#https://leetcode.com/problems/binary-tree-postorder-traversal/
#Title: 145. Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #ITERATIVE SOLUTION
        if root is None:
            return [] 
        
        stack = [root]
        res = []
        
        while stack != []:
            root = stack.pop()
            res.append(root.val)
            if (root.left is not None):
                stack.append(root.left)
            if (root.right is not None):
                stack.append(root.right)
        
        return res[::-1]
        
        
        '''
        #RECURSIVE SOLUTION
        if root is None:
            return []
        return (self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val])
        '''