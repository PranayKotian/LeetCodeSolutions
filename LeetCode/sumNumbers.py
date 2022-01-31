#https://leetcode.com/problems/sum-root-to-leaf-numbers/
#Title: 129. Sum Root to Leaf Numbers
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def allpaths(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [str(node.val)]
            
            val = node.val
            left = allpaths(node.left)
            right = allpaths(node.right)
            for i in range(len(left)):
                left[i] = str(val) + left[i]
            for j in range(len(right)):
                right[j] = str(val) + right[j]
            return left + right
        
        arr = allpaths(root)
        res = 0
        
        for i in arr:
            res += int(i)
            
        return res