#https://leetcode.com/problems/satisfiability-of-equality-equations/
#Title: 990. Satisfiability of Equality Equations
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        #union find solution
        # create connections between vertices that are equal ==
        # if != connection created between vertices in same group, return false
        
        par = [i for i in range(26)]
        rank = [1] * 26
        
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2): 
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2:
                return
            
            if rank[p1] > rank[p2]:
                rank[p1] += 1
                par[p2] = p1
            else: #rank[p1] < rank[p2]:
                rank[p2] += 1
                par[p1] = p2
        
        for i in equations:
            if i[1] == '=':
                union(ord(i[0])-97,ord(i[3])-97)
        for i in equations:
            if i[1] == '!':
                if find(ord(i[0])-97) == find(ord(i[3])-97):
                    return False
        
        return True