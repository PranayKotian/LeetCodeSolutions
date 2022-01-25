#https://leetcode.com/problems/valid-palindrome-ii/
#Title: Valid Palindrome II
#Difficulty: Easy
#Language: Python
#Author: Pranay Kotian

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        for i in range(len(s)//2):
            
            #first occurence of mismatching letter
            if (s[i] != s[len(s) - 1 - i]):
                str1 = s[i:len(s) - 1 - i]
                str2 = s[i+1 : len(s) - i]
                return str1 == str1[::-1] or str2 == str2[::-1]
                
        return True