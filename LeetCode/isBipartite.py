#https://leetcode.com/problems/is-graph-bipartite/
#Title: 785. Is Graph Bipartite?
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        colors = [-1]*n
        
        for i in range(n):
            if colors[i] != -1:
                continue

            queue = []       
            c = True
            queue.append(i)
            while queue:
                for i in range(len(queue)):
                    node = queue.pop(0)
                    if colors[node] == (not c):
                        return False
                    elif colors[node] == c:
                        continue
                    else:
                        for nei in graph[node]:
                            queue.append(nei)    
                        colors[node] = c
                c = not c
        
        return True