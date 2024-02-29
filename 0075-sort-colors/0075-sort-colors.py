class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Solution 1: Inefficient Bubble Sort 
        #Time: O(n^2) Space: O(n)
        
        run = True
        while run:
            run = False
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    run = True