#https://leetcode.com/problems/number-of-operations-to-make-network-connected/
#Title: 1319. Number of Operations to Make Network Connected
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        #union find solution 
        # iterate through connections
        # count number of redundant connections
        # count number of seperate groups
        # min # of changed connections = # of groups - 1
        # if min changed connections > redundant connections --> not enough cables (-1)
        
        #parent and rank arrays for UF
        par = [i for i in range(n)]
        rnk = [1] * n
        
        #counter of redundant connections
        redun = 0
        
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p] 
            return p
            
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2:
                return True
            
            if rnk[p1] > rnk[p2]:
                par[p2] = p1
                rnk[p1] += 1
            else: #rnk[p1] < rnk[p2]:
                par[p1] = p2
                rnk[p2] += 1
        
        #iterate through connections
        for i,j in connections:
            if union(i, j):
                redun += 1
            
        #count # of separate groups
        roots = set()
        for i in range(n):
            roots.add(find(i))
        
        #output
        minConnections = len(roots)-1
        if (minConnections > redun):
            return -1
        return minConnections