#https://leetcode.com/problems/split-a-string-in-balanced-strings/
#Title: Split a String in Balanced Strings
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rCount = 0
        lCount = 0
        balStr = 0
        for i in s:
            if i == 'R':
                rCount += 1
            elif i == 'L':
                lCount += 1
            if rCount == lCount:
                balStr += 1
        return balStr