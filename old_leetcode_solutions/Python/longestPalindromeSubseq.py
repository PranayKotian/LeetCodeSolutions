#https://leetcode.com/problems/longest-palindromic-subsequence/
#Title: 516. Longest Palindromic Subsequence
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == "":
            return 0
        
        #initialize 2D array with longest palindrome of length 1 and 2
        arr = [[1 for i in range(len(s))] for j in range(len(s))]
        
        a = 0
        b = 1
        while a < len(s) and b < len(s):
            if (s[a] == s[b]):
                arr[a][b] = 2 
            else:
                arr[a][b] = 1
            a+=1
            b+=1
        a = 0
        b = 2
        z = 1
        
        #derive all other longest palindromes using DP
        while a < len(s) and b < len(s):
            while a < len(s) and b < len(s):
                if (s[a] == s[b]):
                    arr[a][b] = 2 + arr[a+1][b-1]
                else:
                    arr[a][b] = max(arr[a+1][b], arr[a][b-1])
                a+=1
                b+=1
            z += 1
            a = 0
            b = a + z
        
        return arr[0][len(s)-1]