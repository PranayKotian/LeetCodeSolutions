class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        #Two Pointer Solution
        #Time: O(n) Space: O(1)
        
        s1 = 0
        for c in t:
            if s1 == len(s):
                return True
            if s[s1] == c:
                s1 += 1
        return s1 == len(s)