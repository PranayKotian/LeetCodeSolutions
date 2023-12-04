#https://leetcode.com/problems/number-of-provinces/
#Title: 547. Number of Provinces
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
            
        def union(n1,n2):
            p1 = par[n1]
            p2 = par[n2]
            
            if p1 == p2:
                return
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
            
        
        for i in range(len(isConnected)): 
            for j in range(len(isConnected[i])):
                if (isConnected[i][j] == 1):
                    if i == j:
                        continue
                    union(i+1, j+1)
        
        roots = []
        for a in range(1, n + 1):
            if find(a) not in roots:
                roots.append(find(a)) 
        
        print(par)
        
        return len(roots)
                