# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        #Solution 1: Pre-Order Traversal, Recursive Solution
        #Time: O(n) Space: O(h) where h = tree height (?) 
        
        #Base case: node with no left or right nodes
        if not root.left and not root.right:
            return f"{root.val}"
        
        if root.left and not root.right:
            l = self.tree2str(root.left)
            return f"{root.val}({l})"
        if root.right and not root.left:
            r = self.tree2str(root.right)
            return f"{root.val}()({r})"
        
        l = self.tree2str(root.left)
        r = self.tree2str(root.right)
        return f"{root.val}({l})({r})"