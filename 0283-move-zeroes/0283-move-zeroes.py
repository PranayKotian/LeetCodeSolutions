class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Solution 2: Two Pointer Solution (w/ Swapping)
        #Time: O(n) Space: N/A
        
        l = 0
        for r in range(len(nums)): 
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
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
            
        #Solution 0: Extra Memory Solution
        #Time: O(n) Space: O(n)
        """