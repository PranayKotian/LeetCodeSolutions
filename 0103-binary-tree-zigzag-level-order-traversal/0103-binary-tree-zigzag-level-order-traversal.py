# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #Level Order Traversal
        #Time: O(n) Space: O(n)
        
        if root is None:
            return []
        
        res = []
        level = deque([root])
        flip = False
        while level:
            level_values = []
            for i in range(len(level)):
                node = level.popleft()
                level_values.append(node.val)
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            if flip:
                res.append(level_values[::-1])
                flip = False
            else:
                res.append(level_values)
                flip = True
        return res