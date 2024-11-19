# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #Find Both Paths Solution
        #Time: O(n) Space: O(h)
        
        paths = []
        def find_path(cur, cur_node, search_node):
            if cur_node is None:
                return
            elif cur_node == search_node:
                paths.append(cur+[cur_node])
                return
            find_path(cur+[cur_node], cur_node.left, search_node)
            find_path(cur+[cur_node], cur_node.right, search_node)
        
        find_path([], root, p)
        find_path([], root, q)
        
        minLen = min(len(paths[0]), len(paths[1]))
        for i in range(minLen):
            if paths[0][i] != paths[1][i]:
                return paths[0][i-1]
        return paths[0][minLen-1]
                
        