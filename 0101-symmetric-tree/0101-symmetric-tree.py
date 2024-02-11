# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        #Solution 1: Level Order Traversal
        #Time: O(n) Space: O(n)
        
        level = [root]
        vals = []
        
        while level:
            newLvl = []
            for i in range(len(level)):
                node = level.pop()
                if node is None:
                    vals.append(200)
                    continue
                vals.append(node.val)
                newLvl.append(node.left)
                newLvl.append(node.right)
            if vals != vals[::-1]:
                return False
            vals = []
            level = newLvl
            
        return True