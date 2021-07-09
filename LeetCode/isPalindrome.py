#https://leetcode.com/problems/valid-palindrome/
#Title: 125. Valid Palindrome
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #strip string of all non-letter characters
        #convert all letters to lowercase
        #check if string is palindrome
        
        newstr = ''.join([i for i in s if i.isalnum()])
        newstr = newstr.lower()
        
        for i in range(len(newstr)//2):
            if newstr[i] != newstr[-i - 1]:
                return False
        
        return True
