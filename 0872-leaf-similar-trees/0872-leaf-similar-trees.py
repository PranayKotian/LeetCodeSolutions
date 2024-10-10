# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        #Full Tree Traversal Solution
        #Time: O(n+m) Space: O(n+m)
        
        def addLeaves(node, arr):
            if node.left is None and node.right is None:
                arr.append(node.val)
                return
            if node.left:
                addLeaves(node.left, arr)
            if node.right:
                addLeaves(node.right, arr)
            
        arr1 = []
        arr2 = []
        
        addLeaves(root1, arr1)
        addLeaves(root2, arr2)
        
        return arr1 == arr2