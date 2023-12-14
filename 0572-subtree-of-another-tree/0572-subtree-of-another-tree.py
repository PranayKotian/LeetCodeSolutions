# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Iterate through root tree
        #Check if subtree == subRoot
        if root is None or subRoot is None:
            return False
        def sameTree(p, q):
            if p is None or q is None:
                return p is None and q is None
            return p.val == q.val and sameTree(p.right, q.right) and sameTree(p.left, q.left)
        
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)