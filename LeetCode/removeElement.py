#https://leetcode.com/problems/remove-element/
#Title: Remove Element
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        while (i < len(nums)):
            if (nums[i] == val):
                nums.remove(val)
            else:
                i += 1 
        return i + 1