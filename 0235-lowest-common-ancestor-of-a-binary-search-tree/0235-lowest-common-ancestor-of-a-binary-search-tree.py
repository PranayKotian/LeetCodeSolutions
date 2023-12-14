# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Solution 2
            #search for both nodes
            #track parents of both nodes
            #find the lowest parent
        
        def search(cur: 'TreeNode', parents: 'list', node: 'TreeNode'):
            if cur is None:
                return
            elif node.val == cur.val:
                return (parents + [cur])
            elif cur.val > node.val:
                return search(cur.left, parents+[cur], node)
            else:
                return search(cur.right, parents+[cur], node)
        
        p1 = search(root, [], p)
        q1 = search(root, [], q)
        i = 0
        while i < min(len(p1),len(q1)) and p1[i].val == q1[i].val:
            i += 1
        return p1[i-1]