class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        #Two Pointer Solution
        #Time: O(n) Space: O(1)
        
        if len(s) == 0: return True
        if len(s) > len(t): return False
        
        s1 = 0
        for c in t:
            if s[s1] == c:
                s1 += 1
                if s1 == len(s):
                    return True
        return False