#https://leetcode.com/problems/binary-tree-paths/
#Title: 257. Binary Tree Paths
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [str(root.val)]
            
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        for i in range(len(left)):
            left[i] = str(root.val) + "->" + left[i]
        for j in range(len(right)):
            right[j] = str(root.val) + "->" + right[j]
        
        return left + right