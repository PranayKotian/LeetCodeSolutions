# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        stack = [root]
        while stack:
            newStack = []
            addRes = []
            for node in stack:
                addRes.append(node.val)
                if node.left: newStack.append(node.left)
                if node.right: newStack.append(node.right)
            stack = newStack
            res.append(addRes)
        
        return res