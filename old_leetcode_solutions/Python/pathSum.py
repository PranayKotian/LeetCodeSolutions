#https://leetcode.com/problems/path-sum-ii/
#Title: 113. Path Sum II
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def allpaths(root):
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [[root.val]]
            left = allpaths(root.left)
            right = allpaths(root.right)
            for i in range(len(left)):
                left[i].insert(0, root.val)
            for j in range(len(right)):
                right[j].insert(0, root.val)
            return left + right
            
        arr = allpaths(root)
        print(arr)
        res = []
        
        for i in arr:
            if sum(i) == targetSum:
                res.append(i)
        
        return res