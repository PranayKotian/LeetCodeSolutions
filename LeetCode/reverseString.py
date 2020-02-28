#
#Title: 
#Difficulty:
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st = 0
        ed = len(s) - 1
        
        while (st < ed):
            #Swaps values
            temp = s[st]
            s[st] = s[ed]
            s[ed] = temp
            
            #increments start/end variables
            st = st + 1
            ed = ed - 1