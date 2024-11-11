# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if root is None:
            return "N"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        tree_array = data.split(",")
        self.array_idx = 0
        def build_tree():
            if tree_array[self.array_idx] == "N":
                self.array_idx += 1
                return None
            node = TreeNode(int(tree_array[self.array_idx]))
            self.array_idx += 1
            node.left = build_tree()
            node.right = build_tree()
            return node
        return build_tree()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))