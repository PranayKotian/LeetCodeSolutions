#https://leetcode.com/problems/same-tree/
#100. Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #EFFICIENT SOLUTION
        if p and q:
            return (p.val == q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return p == q
        
        '''
        #MY SOLUTION
        if p is None and q is None:
            return True
        elif p is None or q is None: 
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
        '''