#https://leetcode.com/problems/string-to-integer-atoi/
#Title: String to Integer (atoi)
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def myAtoi(self, str: str) -> int:
        
        '''
        PSEUDOCODE
        1. skip blank spaces
        2. check for negative sign on integer
        3. check for integer 1-9
        4. if first non space char is not an int, return 0
        5. iterate through int values storing them
        6. at last int or first non-int value, return integer
        '''
        
        #skips blank spaces
        i = 0
        while (str[i] == " "):
            i += 1
        
        #checks for negative sign
        mul = 1
        if (str[i] == "-"):
            mul = -1
            i += 1
        
        #returns 0 for non-digit character
        arr = []
        #adds all digits into array
        if (not str[i].isdigit()):
            return 0
        else:
            while(str[i].isdigit()):
                arr.append(str[i])
        
        #Converts array with digits into integer
        num = 0
        length = len(arr)
        for i in arr:
            num += i * 10**length
            length -= 1
        
        #Checks if num is out of bounds
        if (num > (2**31 - 1)):
            return 2**31 - 1
        elif (num < (-2*31)):
            return -2**31
        else:
            return num
        
        #Solution exceeds time limimt
        #Unknown whether solution is correct
