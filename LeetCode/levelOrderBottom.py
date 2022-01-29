#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
#Title: 107. Binary Tree Level Order Traversal II
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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        #level order traversal but flipped at the end
        if root is None:
            return []
        
        res = []
        
        def bfs(level):
            if level == []:
                return
            
            temp = []
            nextlevel = []
            
            for node in level:
                temp.append(node.val)
                if node.left is not None:
                    nextlevel.append(node.left)
                if node.right is not None:
                    nextlevel.append(node.right)
                    
            res.append(temp)
            bfs(nextlevel)
        
        bfs([root])
        return res[::-1]