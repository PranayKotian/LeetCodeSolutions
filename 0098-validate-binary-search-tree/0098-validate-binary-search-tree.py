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
            if node is None:
                return True
            return minVal < node.val < maxVal and validate_BST(node.left, minVal, node.val) and validate_BST(node.right, node.val, maxVal)
        
        return validate_BST(root, ~sys.maxsize, sys.maxsize)