# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Solution 1: check all nodes going down
            #top node is guaranteed to be an ancestor
            #check to see if p and q are connected to current node
            # checking downwards
            #if p or q == current node: return that node
            
        #Solution 2
            #dfs for both nodes
            #take the pointers and move upwards
            #while keeping pointers on the same level
            #when p1 = q1: return that node
            
            #track current level of node
        
        def search(cur: 'TreeNode', parents: 'list', node: 'TreeNode'):
            if cur is None:
                return
            if node.val == cur.val:
                return (parents + [cur])
            
            if search(cur.left, parents+[cur], node):
                return search(cur.left, parents+[cur], node)
            if search(cur.right, parents+[cur], node):
                return search(cur.right, parents+[cur], node)
        
        p1 = search(root, [], p)
        q1 = search(root, [], q)
        
        res = p1[0]
        for i in range(min(len(p1),len(q1))):
            if p1[i].val == q1[i].val:
                res = p1[i]
        return res