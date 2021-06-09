#https://leetcode.com/problems/roman-to-integer/
#Title: Roman to Integer
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        M D C L X V I
        '''
        
        #DICTIONARY SOLUTION
        roman = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        out = roman[s[0]] 
        for i in range(1, len(s)):
            val = roman[s[i]]
            past_val = roman[s[i-1]]
            out += val
            
            if (past_val < val):
                out -= 2 * past_val
            
        return out