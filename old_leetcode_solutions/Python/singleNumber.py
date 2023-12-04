#https://leetcode.com/problems/single-number/
#Title: Single Number
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if (i%2 == 0) and (nums[i] != nums[i+1]):
                return nums[i]
        return nums[len(nums) - 1]

        #ALTERNATE SOLUTION:
        #return 2*sum(set(nums))-sum(nums)