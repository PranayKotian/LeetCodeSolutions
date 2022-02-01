#https://leetcode.com/problems/minimum-depth-of-binary-tree/
#Title: 111. Minimum Depth of Binary Tree
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = [root]
        level = 0
        
        while queue:
            level += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    queue = []
                    break
                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
        
        return level