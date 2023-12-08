class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Binary search solution
        #O(log n) time
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else: 
                l = m+1
        
        #returns insert positions ranging from 0 to len(nums)
        return l