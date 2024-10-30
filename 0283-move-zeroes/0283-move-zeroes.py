class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Track Zeros Approach
        #Time: O(2n) Space: N/A
        
        offset = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                offset += 1
            else:
                nums[i-offset] = nums[i]
        for i in range(len(nums)-offset,len(nums)):
            nums[i] = 0
        
        #Bubble Sort Approach
        #Time: O(n^2) Space: N/A