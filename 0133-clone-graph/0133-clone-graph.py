"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        copy = {node: Node(node.val)}
        stack = [node]
        
        #Copy nodes and connections
        while stack:
            for i in range(len(stack)):
                n = stack.pop()
                for nei in n.neighbors:
                    if nei not in copy:
                        copy[nei] = Node(nei.val)
                        stack.append(nei)
                    copy[n].neighbors.append(copy[nei])
        
        return copy[node]