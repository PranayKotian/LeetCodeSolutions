"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        #DFS Solution
        #Time: O(n) Space: O(n)
        
        cache = {None: None}
        def dfs(cur):
            if cur not in cache:
                cache[cur] = Node(cur.val)
                for nei in cur.neighbors:
                    if nei not in cache:
                        dfs(nei)
                    cache[cur].neighbors.append(cache[nei])
        dfs(node)
        return cache[node]