class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Solution 3: Bucket Sort Solution
        #optimal since we know there are only 3 possible values therefore 3 possible buckets
        #Time: O(n) Space: O(n)
        
        c = {i:0 for i in range(4)}
        for n in nums:
            c[n] += 1
        start,end = 0,c[0]
        for i in range(3):
            for a in range(start,end):
                nums[a] = i
            start,end = end,end+c[i+1]
        
        """
        #Solution 2: Real Bubble Sort
        #Time: O(n^2)   Space: N/A
        
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
        """
        #Solution 1: Inefficient Bubble Sort 
        #Time: O(n^2)   Space: N/A
        #Time: 5%       Space: 62%
        
        run = True
        while run:
            run = False
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    run = True
        """