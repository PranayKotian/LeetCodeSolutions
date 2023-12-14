# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #Solution 1:
        #Time O(n) Space O(1)
        if root is None:
            return []
        
        res = []
        
        def explore(node, curLvl):
            if node is None:
                return
            if curLvl > len(res):
                res.append(node.val)
            explore(node.right, curLvl+1)
            explore(node.left, curLvl+1)
        
        explore(root, 1)
        return res