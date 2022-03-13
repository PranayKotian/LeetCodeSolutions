#https://leetcode.com/problems/rotate-array/
#Title: 189. Rotate Array
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        k = k % len(nums)
        
        for i in range(k):
            temp.append(nums[len(nums)-1])
            nums.pop(len(nums)-1)        
        for j in range(k):
            nums.insert(0, temp[j])