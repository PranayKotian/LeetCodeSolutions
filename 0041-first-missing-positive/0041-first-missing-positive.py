class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #Three Pass Solution
        #Time: O(3n) Space: O(1)
        #Remove all negative nums, set indexes to negative if positive val exists, check for first positive val
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums)+1
        for i in range(len(nums)):
            if abs(nums[i]) > len(nums):
                continue
            nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1
        for i,n in enumerate(nums):
            if n > 0:
                return i+1
        return len(nums)+1