#https://leetcode.com/problems/defanging-an-ip-address/
#Title: Defanging an IP Address
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def defangIPaddr(self, address: str) -> str:
        blank = ""
        for i in address:
            if i == ".":
                blank = blank + "[.]"
            else:
                blank = blank + i
        return blank
    
'''
one line solution:
    return address.replace('.', '[.]')
'''