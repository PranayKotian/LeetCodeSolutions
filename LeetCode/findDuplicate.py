#https://leetcode.com/problems/find-the-duplicate-number/
#Title: Find the Duplicate Number
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if (i > 0) and (nums[i] == nums[i-1]):
                return nums[i]


     """
     ALTERNATE SOLUTION USING DICTIONARY
     dupDict = {}
        for i in nums:
            if (i in dupDict):
                return i
            else:
                dupDict[i] = 1
     """