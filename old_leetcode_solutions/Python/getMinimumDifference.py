#https://leetcode.com/problems/minimum-absolute-difference-in-bst/
#Title: 530. Minimum Absolute Difference in BST
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        arr = inorder(root)
        
        minabs = 10**6
        
        for i in range(1, len(arr)):
            minabs = min(abs(arr[i] - arr[i-1]), minabs)
        
        return minabs