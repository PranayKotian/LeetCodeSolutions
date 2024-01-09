# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node, minVal, maxVal):
            if node is None:
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False
            return traverse(node.left,minVal,node.val) and traverse(node.right,node.val,maxVal)
        
        lowest = -(2**31)-1
        highest = 2**31
        return traverse(root,lowest,highest)