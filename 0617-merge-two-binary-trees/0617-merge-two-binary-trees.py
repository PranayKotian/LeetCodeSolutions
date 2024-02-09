# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #Solution 1: Recursive Solution
        #Time: O(max(n,m)) Space: O(max(n,m))
        
        #Base Cases
        if not root1 and not root2: return None
        if not root1: return root2
        if not root2: return root1
        
        #Recursive Case
        newroot = TreeNode(root1.val+root2.val)
        newroot.left = self.mergeTrees(root1.left, root2.left)
        newroot.right = self.mergeTrees(root1.right, root2.right)
        return newroot