class Solution:
    def countSubstrings(self, s: str) -> int:
        
        #Find Palindromes Solution
        #Time: O(n^2) Space: O(1)
        
        num_palindromes = 1
        for i in range(len(s)-1):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num_palindromes += 1
                l -= 1
                r += 1
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num_palindromes += 1
                l -= 1
                r += 1
        return num_palindromes
            