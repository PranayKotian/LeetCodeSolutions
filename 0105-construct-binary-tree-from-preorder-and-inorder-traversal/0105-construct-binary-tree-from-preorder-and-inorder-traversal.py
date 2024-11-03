# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #Recursive Solution
        #Time: O(n^2) Space: O(n)
        
        #preorder: root {root left right} {root left right}
        #inorder:  {left root right} root {left root right} 
        
        if preorder == []: #or inorder == []
            return None
        res = TreeNode(preorder[0])
        idx = inorder.index(preorder[0]) #number of values in left subtree
        res.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        res.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        return res