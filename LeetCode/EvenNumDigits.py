#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
#Title: Find Numbers with Even Number of Digits
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if (len(str(i)) % 2 == 0):
                count+=1
        return count