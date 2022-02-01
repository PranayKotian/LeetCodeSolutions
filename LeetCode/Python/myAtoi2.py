#https://leetcode.com/problems/string-to-integer-atoi/
#Title: String to Integer (atoi)
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def myAtoi(self, str: str) -> int:
        #Checks for empty string input
        if (len(str) == 0):
            return 0
        
        #Removes initial spaces from input
        i = 0
        while (i < len(str) and str[i] == " "):
            i += 1
        str = str[i:]
        i = 0
        
        #Checks if tring is now empty
        if (len(str) == 0):
            return 0
        
        #Checks if number is negative
        i = 0
        if (str[0] == "-" or str[0] == "+"):
            i += 1
            #Checks if string is now empty
            if (len(str) == 1):
                return 0
        
        #Checks if first non-sign char is a digit
        
        if (not str[i].isdigit()):
            return 0
        
        #Increments i until first non-digit character
        while(i < len(str)):
            if (str[i].isdigit()):
                i += 1
            else:
                break
        
        #Removes trailing non-digit characters
        str = str[:i]
        
        #Checks upper and lower bounds for number
        num = int(str)
        if (num < -2**31):
            return -2**31
        elif(num > 2**31 -1):
            return 2**31 -1
        else:        
            return num 

        #SOLUTION optimized by reducing the number of times string splicing is used
        '''
		Runtime: 28 ms, faster than 89.05% of Python3 online submissions for String to Integer (atoi).
		Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for String to Integer (atoi).
        '''