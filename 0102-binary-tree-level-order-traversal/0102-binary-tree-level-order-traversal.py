# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Solution 1: stack solution
        if root is None:
            return []
        
        res = []
        stack = [root]
        while stack:
            res.append([])
            newStack = []
            for node in stack:
                res[-1].append(node.val)
                if node.left: newStack.append(node.left)
                if node.right: newStack.append(node.right)
            stack = newStack
        
        return res