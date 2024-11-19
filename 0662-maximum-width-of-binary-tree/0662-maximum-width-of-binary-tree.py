# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #Level Order Traversal
        #Time: O(n) Space: O(n)
        
        max_width = 1
        level = deque([(root, 1)])
        
        while level:
            max_width = max(level[-1][1] - level[0][1] + 1, max_width)
            for i in range(len(level)):
                node, node_pos = level.popleft()
                if node.left: level.append((node.left, node_pos*2-1))
                if node.right: level.append((node.right, node_pos*2))
        return max_width