#https://leetcode.com/problems/move-zeroes/
#Title: 283. Move Zeroes
#Difficulty: Easy
#Language: Python
#Author: Pranay Kotian

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zerocount = 0
        for i in nums:
            if i == 0:
                zerocount += 1
        
        for j in range(zerocount):
            nums.remove(0)
        for k in range(zerocount):
            nums.append(0)