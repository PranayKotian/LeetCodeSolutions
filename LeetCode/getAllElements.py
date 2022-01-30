#https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
#Title: 1305. All Elements in Two Binary Search Trees
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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        #SOLUTION WITH PYTHON .SORT()
        return sorted(inorder(root1) + inorder(root2))
        
        #SOLUTION WITHOUT PYTHON SORT
#         arr1 = inorder(root1)
#         arr2 = inorder(root2)
#         res = []
        
#         p1 = 0
#         p2 = 0
#         while p1 != len(arr1) and p2!=len(arr2):
#             if arr1[p1] < arr2[p2]:
#                 res.append(arr1[p1])
#                 p1 += 1
#             else:
#                 res.append(arr2[p2])
#                 p2 += 1
#         while p1 != len(arr1):
#             res.append(arr1[p1])
#             p1 += 1
#         while p2 != len(arr2):
#             res.append(arr2[p2])
#             p2 += 1
        
#         return res