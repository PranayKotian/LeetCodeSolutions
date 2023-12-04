#https://leetcode.com/problems/binary-tree-level-order-traversal/
#Title: 103. Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        def bfs(level, zig):
            if level == []:
                return
            
            temp = []
            nextlevel = []
            
            for node in level:
                temp.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            
            if zig:
                res.append(temp)
                bfs(nextlevel, False)
            else: #zag
                res.append(temp[::-1])
                bfs(nextlevel, True)
        
        res = []
        bfs([root], True)
        
        return res 