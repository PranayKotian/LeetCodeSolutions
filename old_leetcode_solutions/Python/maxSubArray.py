#https://leetcode.com/problems/maximum-subarray/
#Title: 53. Maximum Subarray
#Difficulty: Easy
#Language: Python
#Author: Pranay Kotian

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        output = nums[0]
        
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            output = max(curSum, output)
        
        return output