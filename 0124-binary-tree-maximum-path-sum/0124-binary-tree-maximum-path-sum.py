# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        #Solution 1: DFS (check all paths)
        #For each node, calculate the maxPathSum starting from that node
        
        maxPaths = {None: 0}
        
        def maxPath(node):
            if node is None:
                return 0
            maxleft = maxPath(node.left)
            maxright = maxPath(node.right)
            maxPaths[node] = node.val + max(0, maxleft, maxright)
            return maxPaths[node]
        
        maxPath(root)
        
        res = ~sys.maxsize
        stack = [root]
        
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                curVal = node.val
                if node.left: 
                    curVal += max(0, maxPaths[node.left])
                    stack.append(node.left)
                if node.right:
                    curVal += max(0, maxPaths[node.right])
                    stack.append(node.right)
                res = max(res, curVal)
        
        return res
                