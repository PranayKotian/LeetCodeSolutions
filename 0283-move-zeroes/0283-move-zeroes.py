class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Solution 1: Two Pointer Solution
        #Time: O(n) Space: N/A 
        
        i = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                continue
            elif r == i: #and nums[r] != 0
                i += 1
                continue
            nums[i] = nums[r]
            i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1