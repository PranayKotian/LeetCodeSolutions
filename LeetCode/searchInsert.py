#https://leetcode.com/problems/search-insert-position/
#Title: Search Insert Position
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1
        found = False
        while (min <= max and not found):
            mid = (min + max) // 2
            if nums[pos] == target:
                return pos
            else:   
                if (nums[mid] < target):
                    min = pos + 1 
                else (nums[mid] > target):
                    max = pos - 1
            if ():
                return max
            