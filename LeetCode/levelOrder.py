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
        
        '''
        #ITERATIVE SOLUTION 
        res = []
        
        queue = [root]
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(temp)
            
        return res
        '''

        res = []
        
        def bfs(rootslist):
            if rootslist == []:
                return
            
            add = []
            newrootslist = []
            for node in rootslist:
                add.append(node.val)
                if (node.left is not None):
                    newrootslist.append (node.left)
                if (node.right is not None):
                    newrootslist.append (node.right)
            res.append(add)
            
            bfs(newrootslist)
            
        bfs([root])
        return res