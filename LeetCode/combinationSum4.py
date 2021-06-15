#https://leetcode.com/problems/combination-sum-iv/
#Title: 377. Combination Sum IV
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        arr = [0 for _ in range(target + 1)]
        arr[0] = 1
        
        for i in range(1, len(arr)):
            for j in range(len(nums)):
                if (i - nums[j] < 0):
                    break
                arr[i] += arr[i - nums[j]]
        
        return arr[target]