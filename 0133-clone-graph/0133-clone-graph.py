"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        #Solution 1: Original to Clone Dict w/ BFS
        #Time: O(n) Space: O(n)
        if node is None:
            return None
        
        clone = {}
        clone[node] = Node(node.val)
        stack = [node]
        
        while stack:
            cur = stack.pop()
            for n in cur.neighbors:
                if n not in clone:
                    stack.append(n)
                    clone[n] = Node(n.val)
                clone[cur].neighbors.append(clone[n])
        
        return clone[node]