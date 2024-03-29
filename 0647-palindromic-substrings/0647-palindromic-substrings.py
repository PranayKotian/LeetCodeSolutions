class Solution:
    def countSubstrings(self, s: str) -> int:
        
        #Solution 1: Odd and Even length palindromes
        def countPalis(l,r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        
        res = 0
        for i in range(len(s)):
            res += countPalis(i,i)
            res += countPalis(i,i+1)
        return res