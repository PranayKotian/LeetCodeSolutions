# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodCheck(node, curmax):
            if node is None:
                return 0
            if node.val >= curmax:
                goodVal = 1
                curmax = node.val
            else:
                goodVal = 0
            return goodVal + goodCheck(node.left, curmax) + goodCheck(node.right, curmax)
        
        return goodCheck(root, -10**4)