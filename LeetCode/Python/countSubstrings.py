#https://leetcode.com/problems/palindromic-substrings/
#Title: 647. Palindromic Substrings
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        self.count = 0
        
        def check(a,b):
            while a >= 0 and b < len(s) and s[a] == s[b]:
                self.count += 1
                a -= 1
                b += 1
        
        for i in range(len(s)):
            self.count += 1
            
            check(i, i+1)
            check(i-1,i+1)
        
        return self.count