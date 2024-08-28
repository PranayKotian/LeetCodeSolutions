class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        
        #Adjacency List Solution
        #Time: O(n) Space: O(n)
        
        trusts = {i:[] for i in range(1,n+1)}
        trustedBy = {i:[] for i in range(1,n+1)} 
        
        for t1,t2 in trust:
            trusts[t1].append(t2)
            trustedBy[t2].append(t1)
        
        for p in trustedBy:
            if len(trustedBy[p]) == n-1 and len(trusts[p]) == 0:
                return p
        return -1