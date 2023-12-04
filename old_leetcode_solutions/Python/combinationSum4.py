#https://leetcode.com/problems/combination-sum-iv/
#Title: 377. Combination Sum IV
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        arr = [-1] * (target)
        
        #given a starting value, do any of the nums + starting value add up to target
        #@lru_cache(None)
        def combins(startval, nums):
            if startval > target:
                return 0
            elif startval == target:
                return 1
            if arr[startval] != -1:
                return arr[startval]
        
            res = 0
            for n in nums:
                res += combins(startval+n, nums)
            
            arr[startval] = res
            return res
        
        return combins(0, nums)