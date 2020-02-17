#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#Title: Remove Duplicates from Sorted Array
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while (i < len(nums) - 1):
            if (nums[i] == nums[i+1]):
                nums.remove(nums[i])
            else:
                i += 1 
        return i + 1 