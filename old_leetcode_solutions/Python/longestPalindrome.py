#https://leetcode.com/problems/longest-palindromic-substring/
#Title: 5. Longest Palindromic Substring
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #DP solution
        #O(n^2) time
        if len(s) == 0:
            return ""
        
        self.output = s[0]
        
        def check(a,b):
            while a >= 0 and b < len(s):
                if (s[a] == s[b]):
                    if (1 + b - a > len(self.output)):
                        self.output = s[a:b+1]
                    a -= 1
                    b += 1
                else:
                    break
        
        for i in range(len(s)):
            #checks all odd sized palindromes
            check(i-1,i+1)
            
            #checks all even sized palindromes
            check(i-1,i)
        
        return self.output

        #brute force solution (time limit exceeded)
        #O(n^3) time
        """
        if len(s) == 1 or len(s) == 0:
            return s
        
        output = ""
        
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    if len(sub) > len(output):
                        output = sub
        
        return output
        """