#https://leetcode.com/problems/reverse-integer/
#Title: Reverse Integer
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def reverse(self, x: int) -> int:
        #Removes negative sign from number
        mult = 1
        if (x < 0):
            mult = -1
            x = -1 * x
        
        #Removes trailing zeros
        while (x % 10 == 0):
            x = x // 10
            
        #Reverses numbers
        num = 0
        for i in range(len(str(x)) - 1, -1, -1):
            num += (x % 10) * (10**i)
            x = x // 10
            
        return num * mult
        
        #PASSES test cases
        #Exceeds time limit on final submission