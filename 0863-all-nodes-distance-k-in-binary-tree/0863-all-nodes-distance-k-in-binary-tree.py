# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        #Two Pass Solution
        #First pass: find target node, and store all node:parent node information in hashmap
        #Second pass: from target node, BFS/DFS to find all nodes distance k from target node
        #Time: O(n) Space: O(n)
        
        parent = {root:None}
        def mapParents(node):
            if node is None:
                return
            if node.left: 
                parent[node.left] = node
                mapParents(node.left)
            if node.right: 
                parent[node.right] = node
                mapParents(node.right)
        mapParents(root)
        
        res = []
        visited = set()
        def kDistanceNodes(node, dist):
            if node is None or node in visited:
                return
            if dist == 0:
                res.append(node.val)
                return
            visited.add(node)
            kDistanceNodes(node.left, dist-1)
            kDistanceNodes(node.right, dist-1)
            kDistanceNodes(parent[node], dist-1)
            visited.remove(node)
            
        kDistanceNodes(target,k)
        return res
        