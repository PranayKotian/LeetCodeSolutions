class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #Union Find Solution
        #Time: O(n) Space: O(n) 
        
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)
        
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
            
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] ++ rank[p1]
            return 1
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]