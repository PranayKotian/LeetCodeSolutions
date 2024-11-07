# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #DFS Solution (add smallest values first)
        #Return when len(arr) == k
        #Time: O(n) Space: O(n)
        
        res = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left) 
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res[k-1]