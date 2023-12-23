class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #Solution 1: Brute Force Method (Time O(n^2))
            #Check all possible substrings
            
        #Solution 2: Dynamic Programming (Time >O(n))
        res = ""
        for i in range(len(s)):
            #Checks odd number palindromes
            l = i-1
            r = i+1
            while l >= 0 and r < len(s) and s[l:r+1] == s[l:r+1][::-1]:
                l -= 1
                r += 1
            if r-l-1 > len(res):
                res = s[l+1:r]
        
            #Checks even number palindromes
            l = i-1
            r = i
            while l >= 0 and r < len(s) and s[l:r+1] == s[l:r+1][::-1]:
                l -= 1
                r += 1
            if r-l-1 > len(res):
                res = s[l+1:r]
        return res