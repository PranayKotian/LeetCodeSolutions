class Solution:
    def numDecodings(self, s: str) -> int:
        
        #Dynamic Programming Solution
        #Time: O(n) Space: O(1)
        
        valid = set([str(i) for i in range(1,27)])
        c1, c2 = 1, 0
        if s[0] in valid:
            c2 = 1
        for i in range(1, len(s)):
            c3 = 0
            if s[i] in valid:
                c3 += c2
            if s[i-1:i+1] in valid:
                c3 += c1
            c1, c2 = c2, c3
        return c2