class Solution:
    def numDecodings(self, s: str) -> int:
        
        #DP Solution
        #Time: O(n) Space: O(1)
        
        valid = set([str(i) for i in range(1,27)])
        p1 = 1 if s[-1] in valid else 0
        p2 = 1
        
        for i in range(len(s)-2,-1,-1):
            if s[i] in valid:
                if s[i:i+2] in valid:
                    p1,p2 = p1+p2, p1
                else:
                    p1,p2 = p1,p1
            else:
                p1,p2 = 0,p1
        return p1