#https://leetcode.com/problems/remove-element/
#Title: Remove Element
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Identical solution to remove duplicates problem
        i = 0 
        while (i < len(nums)):
            if (nums[i] == val):
                nums.remove(val)
            else:
                i += 1 
        return i + 1

        """
        Runtime: 28 ms, faster than 84.57% of Python3 online submissions for Remove Element.
		Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Element.
        """