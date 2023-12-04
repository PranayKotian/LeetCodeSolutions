#https://leetcode.com/problems/clone-graph/
#Title: 133. Clone Graph
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
                
        #------DFS Recursive Solution------
        
        #maps old nodes to new nodes
        hashmap = {}
        
        def clone(node):
            #checks if node already exists in old to new hashmap
            if node in hashmap:
                return hashmap[node]
            
            #creates copy of node (with index value)
            copy = Node(node.val)
            #adds it to the old to new hashmap
            hashmap[node] = copy
            
            #iterates through all the node's neighbors
            for i in node.neighbors:
                #adds copies of the node's neighbors to the node being copied in this iteration 
                copy.neighbors.append(clone(i))
            
            return copy
        
        return clone(node) if node else None

                #------DFS Solution------
        
#         if not node:
#             return None
        
#         oldtonew = {node: Node(node.val)}
#         stack = [node]
        
#         while stack:
#             n = stack.pop()
#             for neigh in n.neighbors:
#                 if neigh not in oldtonew:
#                     stack.append(neigh)
#                     oldtonew[neigh] = Node(neigh.val)
#                 oldtonew[n].neighbors.append(oldtonew[neigh])
        
#         return oldtonew[node]

        #------BFS Solution------
    
#         if not node:
#             return None
        
#         m = {node: Node(node.val)}
#         queue = [node]
        
#         while queue:
#             n = queue.pop(0)
#             for neigh in n.neighbors:
#                 if neigh not in m:
#                     queue.append(neigh)
#                     m[neigh] = Node(neigh.val)
#                 m[n].neighbors.append(m[neigh])
        
#         return m[node]