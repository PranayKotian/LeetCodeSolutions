#https://leetcode.com/problems/binary-tree-inorder-traversal/
#Title: 94. Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right))