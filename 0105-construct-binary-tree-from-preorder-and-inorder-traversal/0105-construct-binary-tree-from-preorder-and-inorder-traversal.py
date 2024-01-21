# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #Recursive solution
        #Preoder: M L R
        #Inorder: L M R
        
        if not preorder or not inorder:
            return None
        rootVal = preorder[0]
        m = inorder.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.buildTree(preorder[1:1+m], inorder[:m])
        root.right = self.buildTree(preorder[1+m:], inorder[m+1:])
        return root