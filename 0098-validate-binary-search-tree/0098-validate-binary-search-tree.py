# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #Recursive Solution
        #Time: O(n) Space: O(h)
        
        def validate_BST(node: Optional[TreeNode], minVal: int, maxVal: int):
            res = minVal < node.val < maxVal
            if node.left: res = res and validate_BST(node.left, minVal, node.val)
            if node.right: res = res and validate_BST(node.right, node.val, maxVal)
            return res
        
        return validate_BST(root, ~sys.maxsize, sys.maxsize)