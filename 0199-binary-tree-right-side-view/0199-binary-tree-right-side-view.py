# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Solution 2: level order traversal
        #take rightmost value of each level
        res = []
        q = deque([root])
        while q:
            n = len(q)
            right = None
            for i in range(n):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                res.append(right.val)
        return res