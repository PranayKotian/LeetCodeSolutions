class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        #Sorting + Two Pointer Solution
        #Time: O(nlogn) Space: O(n)
        
        g.sort()
        s.sort()
        res = 0
        
        gp = len(g)-1
        sp = len(s)-1
        
        while gp >= 0 and sp >= 0:
            if s[sp] >= g[gp]:
                res += 1
                sp -= 1
                gp -= 1 
            if s[sp] < g[gp]:
                gp -= 1
        
        return res