#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#Title: 230. Kth Smallest Element in a BST
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #EFFICIENT SOLUTION
        def helper(node):
            if not node:
                return
            helper(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            helper(node.right)
        
        self.k = k
        self.res = None
        helper(root)
        return self.res
        
        #SIMPLE RECURSIVE SOLUTION (convert BST into array and find element at index k-1)
        '''
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        return inorder(root)[k-1]
        '''