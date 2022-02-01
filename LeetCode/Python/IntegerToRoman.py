#https://leetcode.com/problems/integer-to-roman/
#Title: Integer to Roman
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def intToRoman(self, num: int) -> str:
        romNum = ''
        
        #I = 1
        #IV = 4
        #V = 5
        #IX = 9
        #X = 10
        #XL = 40
        #XC = 90
        #CD = 400
        #CM = 900
                
        while (num >= 1000):
            num-= 1000
            romNum += "M"
        if (num >= 900):
            num-= 900
            romNum += "CM"
        while (num >= 500):
            num-= 500
            romNum += "D"
        if (num >= 400):
            num-= 400   
            romNum += "CD"
        while (num >= 100):
            num-= 100
            romNum += "C"
        if (num >= 90):
            num-= 90   
            romNum += "XC"
        while (num >= 50):
            num-= 50
            romNum += "L"
        if (num >= 40):
            num-= 40   
            romNum += "XL"
        while (num >= 10):
            num-= 10
            romNum += "X"
        if (num >= 9):
            num-= 9   
            romNum += "IX"
        while (num >= 5):
            num-= 5
            romNum += "V"
        if (num >= 4):
            num-= 4
            romNum += "IV"
        while (num >= 1):
            num-= 1
            romNum += "I"
            
        return romNum