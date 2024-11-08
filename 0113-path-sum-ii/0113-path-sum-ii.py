# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        #Recursive Solution
        #Time: O(n) Space: O(h)
        
        #Recursive go through tree
        #Add values to path, and subtract the values from the target value
        #Once path reaches leaf node (node == None) if target == 0: add path to result
        
        res = []
        def paths(node, target, path):
            if node is None:
                return
            if node.left is None and node.right is None: #leaf node check
                if target == node.val:
                    res.append(path+[node.val])
                return
            if node.left: paths(node.left, target-node.val, path+[node.val])
            if node.right: paths(node.right, target-node.val, path+[node.val])
        
        paths(root, targetSum, [])
        return res