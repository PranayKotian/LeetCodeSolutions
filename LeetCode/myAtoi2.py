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
        
        #Checks if string is now empty
        if (not i < len(str)):
            return 0
        
        #Checks if number is negative
        i = 0
        if (str[0] == "-" or str[0] == "+"):
            i += 1
        
        #Checks if string is now empty
        if (not i < len(str)):
            return 0
        #Checks if first non-sign char is a digit
        if (not str[i].isdigit()):
            return 0
        
        while(i < len(str)):
            if (str[i].isdigit()):
                i += 1
            else:
                break
        
        str = str[:i]
        
        if (int(str) < -2**31):
            return -2**31
        elif(int(str) > 2**31 -1):
            return 2**31 -1
        else:        
            return int(str) 


        #SOLUTION can be improved by finding a better way to actively
        # check whether the string is empty instead of using
        # multiple checks after each step