# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        #Solution 2: Inorder Traversal w/o Extra Memory
        #Time: O(n) Space: O(1)
        prev = None
        res = sys.maxsize
        
        def dfs(node):
            if node is None:
                return
            nonlocal prev, res
            dfs(node.left)
            if prev:
                res = min(res, node.val-prev.val)
            prev = node
            dfs(node.right)
        dfs(root)
        return res
        
        """
        #Solution 1: Inorder Traversal w/ Extra Memory
        #Time: O(n) Space: O(n)
        
        def inorder(node):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        res = inorder(root)
        minDiff = res[1]-res[0]
        for i in range(2,len(res)):
            minDiff = min(minDiff, res[i]-res[i-1])
        return minDiff
        """