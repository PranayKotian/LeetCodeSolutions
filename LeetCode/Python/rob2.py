#https://leetcode.com/problems/house-robber-ii/
#Title: 213. House Robber II
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 2:
                return nums[0]
        
        if (n%2 == 0):
            arr = [0 for i in range(n)]
            arr[0] = nums[0]
            arr[1] = max(nums[0], nums[1])

            for i in range(2, n):
                arr[i] = max(arr[i-1], arr[i-2] + nums[i])

            return arr[n-1]
    
        else:
            nums1 = nums[1:n]
            nums2 = nums[0:n-1]