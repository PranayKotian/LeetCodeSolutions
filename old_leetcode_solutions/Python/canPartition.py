#https://leetcode.com/problems/partition-equal-subset-sum/
#Title: 416. Partition Equal Subset Sum
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2 == 1:
            return False
        
        halfsum = sum(nums)//2
        
        arr = [False for i in range(halfsum+1)]
        arr[0] = True
        
        for n in nums:
            clone = arr.copy()
            for i in range(n,halfsum+1):
                if clone[i-n] == True:
                    arr[i] = True
            if arr[halfsum]:
                return True
        
        return False