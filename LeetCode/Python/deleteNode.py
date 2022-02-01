#https://leetcode.com/problems/delete-node-in-a-bst/
#Title: 450. Delete Node in a BST
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key == root.val:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None: 
                return root.left
            else:
                pnt = root.left
                while pnt.right:
                    pnt = pnt.right
                root.val = pnt.val
                root.left = self.deleteNode(root.left, pnt.val)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        return root
        
        