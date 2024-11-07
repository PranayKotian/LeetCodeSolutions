# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #Iterative DFS Solution
        #Time: O(n) Space: O(k)
        
        cur = root
        stack = []
        res = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            res.append(cur.val)
            if k == 0:
                return (res[-1])
            cur = cur.right
        return -1 #error
        
        """
        #Recursive DFS Solution (add smallest values first)
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
        """