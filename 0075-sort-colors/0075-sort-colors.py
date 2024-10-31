class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Bubble Sort
        #Time: O(n^2) Space: N/A
        
        for j in range(1,len(nums)):
            for i in range(len(nums)-j):
                if nums[i+1] < nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]