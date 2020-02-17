#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#Title: Remove Duplicates from Sorted Array
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        #loop runs until increment reaches the second last element
        # final if condition checks if the second last element equals the last element (last possible duplicate)
        while (i < len(nums) - 1):
            if (nums[i] == nums[i+1]):
                nums.remove(nums[i])
            #if no duplicate, counter increments to next element
            else:
                i += 1
        #increment i starts at 0 so length will be i + 1
        return i + 1 

        """
        Runtime: 568 ms, faster than 8.16% of Python3 online submissions for Remove Duplicates from Sorted Array.
		Memory Usage: 14.4 MB, less than 98.36% of Python3 online submissions for Remove Duplicates from Sorted Array.
        """
