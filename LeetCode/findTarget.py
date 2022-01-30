#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
#Title: 653. Two Sum IV - Input is a BST
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def traverse(node):
            if not node:
                return []
            return(traverse(node.left) + [node.val] + traverse(node.right))
        
        arr = traverse(root)
        
        p1 = 0
        p2 = len(arr) - 1
        
        while p1 < p2:
            tot = arr[p1] + arr[p2]
            if tot < k:
                p1 += 1
            elif tot == k:
                return True
            else:
                p2 -= 1
        
        return False