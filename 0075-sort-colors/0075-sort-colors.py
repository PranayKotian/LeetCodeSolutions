class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Solution 2: Real Bubble Sort
        #Time: O(n^2)   Space: O(n)
        #Time: 61%      Space: 35%
        
        n = len(nums)
        for i in range(n-1):
            run = False
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    run = True
            if not run:
                break
        
        """
        #Solution 1: Inefficient Bubble Sort 
        #Time: O(n^2)   Space: O(n)
        #Time: 5%       Space: 62%
        
        run = True
        while run:
            run = False
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    run = True
        """