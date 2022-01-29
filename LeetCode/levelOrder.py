#https://leetcode.com/problems/binary-tree-level-order-traversal/
#Title: 102. Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = [[root.val]]
        
        def bfs(rootslist):
            temp = []
            newrootslist = []
            
            for node in rootslist:
                if (node.left is not None):
                    newrootslist.append (node.left)
                    temp.append(node.left.val)
                if (node.right is not None):
                    newrootslist.append (node.right)
                    temp.append(node.right.val)
            
            if temp != []:
                res.append(temp)
            if newrootslist != []:
                bfs(newrootslist)
            
        bfs([root])
        return res