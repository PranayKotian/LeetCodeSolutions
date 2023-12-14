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
        q = deque([root])
        while q:
            res.append([])
            for i in range(len(q)):
                node = q.popleft()
                res[-1].append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return res