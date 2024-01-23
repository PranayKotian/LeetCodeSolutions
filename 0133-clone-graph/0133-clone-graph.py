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
        
        startToEnd = {}
        stack = [node]
        
        #Copy nodes
        while stack:
            for i in range(len(stack)):
                n = stack.pop()
                if n not in startToEnd:
                    startToEnd[n] = Node(n.val)
                for nei in n.neighbors:
                    if nei not in startToEnd:
                        stack.append(nei)
        
        #Copy connections
        for n in startToEnd:
            for nei in n.neighbors:
                startToEnd[n].neighbors.append(startToEnd[nei])
        
        return startToEnd[node]