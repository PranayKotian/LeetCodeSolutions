#https://leetcode.com/problems/range-sum-of-bst/
#Title: 938. Range Sum of BST
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        arr = inorder(root)
        tot = 0
        
        for i in arr:
            if low <= i <= high:
                tot += i
            if i > high:
                break
        
        return tot
        
        '''
        #RECURSESIVE SOLUTION
        if root is None:
            return 0
        
        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)     
        elif root.val < low:
            return self.rangeSumBST(root.right,low,high)
        else: #root.val > high:
            return self.rangeSumBST(root.left,low,high)
        '''