class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Time: O(logn)
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        #find minimum (finding the rotation)
        l = 1
        r = len(nums)-1
        rotation = 0
        
        while l <= r:
            m = (l+r)//2
            if nums[m] < nums[m-1]:
                rotation = len(nums)-m
                break
            elif nums[m] > nums[0]:
                l = m+1
            else:
                r = m-1
        
        #normal binary search
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m-rotation] == target:
                return (len(nums)+m-rotation)%len(nums)
            elif nums[m-rotation] > target:
                r = m-1
            else:
                l = m+1
        
        return -1