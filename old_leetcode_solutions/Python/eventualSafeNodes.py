#https://leetcode.com/problems/find-eventual-safe-states/
#Title: 802. Find Eventual Safe States
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        #number of nodes in graph
        n = len(graph)
        #tracks unvisited, visisted (safe), and cyclic nodes (not safe)
        color = [0] * n
        output = []
        
        def dfs(n):
            if color[n]: #if color is non zero, check if the color is 1 (safe) or 2 (non safe)
                return color[n] == 1
            color[n] = 2 #node is marked as unsafe until proven safe
            for i in graph[n]:
                if not dfs(i): #if child node is unsafe, parent node is unsafe
                    return False
            color[n] = 1
            return True
            
        for i in range(n):
            if dfs(i):
                output.append(i)
        
        return output