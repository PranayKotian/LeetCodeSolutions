#https://leetcode.com/problems/range-sum-of-bst/
#Title: 669. Trim a Binary Search Tree
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if low <= root.val <= high:
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
        else: #root.val not within low-high bounds
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return self.trimBST(root.right,low,high)
            elif root.right is None:
                return self.trimBST(root.left,low,high)
            else: #root has left and right nodes
                if root.val < low:
                    return self.trimBST(root.right,low,high)
                else: #root.val > high
                    return self.trimBST(root.left,low,high)
        
        return root