#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#Title: Find Minimum in Rotated Sorted Array
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #CHEATING SOLUTION
        #O(n log n) time
        # nums.sort()
        # return nums[0]
        
        #PROPER SOLUTION (MODIFIED BINARY SEARCH)
        #O(log n)
        
        n = len(nums)
        
        #if list is just one element
        if (n == 1):
            return nums[0]
        
        #if list is unrotated, last elm will be larger than first
        if (nums[n-1] > nums[0]):
            return nums[0]
        
        bot = 1
        top = n - 1
            
        while (top >= bot):
            mid = (bot + top) // 2
            if (nums[mid] < nums[mid-1]):
                return nums[mid]
            
            if (nums[mid] > nums[top]):
                bot = mid + 1
            elif (nums[mid] < nums[top]):
                top = mid - 1
            